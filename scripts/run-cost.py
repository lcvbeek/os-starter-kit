#!/usr/bin/env python3
"""Attribute a Claude Code run's token spend to the tools that caused it.

Reads the session transcript (JSONL) that Claude Code writes as it works, and
emits a markdown block for a skill's run log.

Usage:
    python3 scripts/run-cost.py                  # this session (CLAUDE_TRANSCRIPT_PATH, set by the
                                                 # SessionStart hook), else newest for this project
    python3 scripts/run-cost.py --transcript P   # a specific one
    python3 scripts/run-cost.py --json           # machine-readable

Subagents (Agent tool) write their own transcripts under <session>/subagents/.
Their cost is added to the total and listed per subagent with its model, so a
switch to a cheaper subagent model shows up in the log. Logs before 2026-10-12
left subagents out entirely.

How attribution works, and where it is honest:

  Every assistant turn's `usage` says what that turn cost. A tool's cost is not
  its own turn — it is the tokens its *result* adds to the NEXT turn's input.
  So the marginal input of turn N+1 (raw input + cache writes) is split across
  the tool results returned since turn N, in proportion to their size.

  `cache_read_input_tokens` is deliberately NOT attributed to any tool. It is
  the cost of re-reading the conversation so far — the carry. In a long
  agentic run it is usually the largest line, and pinning it on whichever tool
  happened to run last would be a lie. A run that looks expensive with a small
  tool table is telling you the conversation is too long, not that a tool is
  too greedy.

Dollar figures are list-price estimates computed locally, the same way
Claude Code's own /usage does it. On a subscription nothing is billed per
token, so read them as a size signal, not an invoice.
"""

import argparse, json, os, sys, glob, collections

# USD per million tokens. Cache read = 0.1x input unless CACHE_READ_USD says otherwise;
# cache write = 1.25x (5m) / 2x (1h). Rates from the claude-api skill's model table (2026-10-06).
PRICES = {
    "claude-opus-5-5":  (4.00, 20.00),
    "claude-opus-5":    (5.00, 25.00),
    "claude-opus-4-8":  (5.00, 25.00),
    "claude-sonnet-5-5": (2.00, 10.00),
    "claude-sonnet-5":  (2.00, 10.00),
    "claude-haiku-5-5": (0.10,  0.50),
    "claude-haiku-4-5": (1.00,  5.00),
    "claude-fable-5-1": (10.00, 50.00),
}
CACHE_READ_USD = {"claude-opus-5-5": 0.20}
# Haiku 5.5 bills a turn whose prompt exceeds 100k tokens at $0.50 / $2.50.
LONG_PROMPT = {"claude-haiku-5-5": (100_000, 0.50, 2.50)}
CACHE_READ, WRITE_5M, WRITE_1H = 0.10, 1.25, 2.00


def price(model, u):
    base_in, base_out = PRICES.get(model, (0.0, 0.0))
    cc = u.get("cache_creation") or {}
    w5 = cc.get("ephemeral_5m_input_tokens", 0)
    w1 = cc.get("ephemeral_1h_input_tokens", 0)
    if not (w5 or w1):
        w5 = u.get("cache_creation_input_tokens", 0)
    read_rate = CACHE_READ_USD.get(model, base_in * CACHE_READ)
    if model in LONG_PROMPT:
        limit, long_in, long_out = LONG_PROMPT[model]
        prompt = u.get("input_tokens", 0) + u.get("cache_read_input_tokens", 0) + w5 + w1
        if prompt > limit:
            base_in, base_out = long_in, long_out
            read_rate = long_in * CACHE_READ
    return (
        u.get("input_tokens", 0) * base_in
        + u.get("cache_read_input_tokens", 0) * read_rate
        + w5 * base_in * WRITE_5M
        + w1 * base_in * WRITE_1H
        + u.get("output_tokens", 0) * base_out
    ) / 1_000_000


def blocks(msg):
    c = msg.get("content")
    return c if isinstance(c, list) else []


def size(block):
    c = block.get("content")
    if isinstance(c, str):
        return len(c)
    if isinstance(c, list):
        return sum(len(p.get("text", "")) if isinstance(p, dict) else len(str(p)) for p in c)
    return len(json.dumps(c)) if c is not None else 0


def find_transcript():
    own = os.environ.get("CLAUDE_TRANSCRIPT_PATH")  # set by .claude/hooks/session-start.sh
    if own and os.path.exists(own):
        return own
    slug = os.getcwd().replace("/", "-")
    for base in (os.path.expanduser("~/.claude/projects"), "/root/.claude/projects"):
        hits = glob.glob(os.path.join(base, slug, "*.jsonl")) + glob.glob(os.path.join(base, slug + "*.jsonl"))
        if hits:
            return max(hits, key=os.path.getmtime)
    return None


def analyse(path):
    events = []
    for line in open(path, encoding="utf-8", errors="replace"):
        line = line.strip()
        if line:
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                pass

    tool_of = {}                                  # tool_use_id -> tool name
    calls = collections.Counter()                 # tool -> call count
    result_bytes = collections.Counter()          # tool -> bytes returned
    attributed = collections.Counter()            # tool -> marginal input tokens
    totals = collections.Counter()
    by_model = collections.defaultdict(collections.Counter)
    cost = collections.defaultdict(float)
    pending = []                                  # tool results awaiting the next assistant turn
    turns = 0
    seen = set()                                  # assistant message ids already counted

    for ev in events:
        msg = ev.get("message")
        if not isinstance(msg, dict):
            continue

        if ev.get("type") == "user":
            for b in blocks(msg):
                if b.get("type") == "tool_result":
                    name = tool_of.get(b.get("tool_use_id"), "unknown")
                    n = size(b)
                    result_bytes[name] += n
                    pending.append((name, n))

        elif ev.get("type") == "assistant":
            # Claude Code writes one event per content block (thinking, text,
            # tool_use) and repeats the same usage on each. Count usage once per
            # message id, or every turn is billed 2-3x and the repeats land in
            # "(prompt overhead)" because the first copy already took the results.
            mid = msg.get("id")
            u = msg.get("usage") or {}
            if mid and mid in seen:
                u = {}
            elif mid:
                seen.add(mid)
            if u:
                turns += 1
                model = msg.get("model", "unknown")
                cc = u.get("cache_creation") or {}
                w5 = cc.get("ephemeral_5m_input_tokens", 0)
                w1 = cc.get("ephemeral_1h_input_tokens", 0)
                if not (w5 or w1):
                    w5 = u.get("cache_creation_input_tokens", 0)
                row = {
                    "input": u.get("input_tokens", 0),
                    "cache_read": u.get("cache_read_input_tokens", 0),
                    "write_5m": w5, "write_1h": w1,
                    "output": u.get("output_tokens", 0),
                    "thinking": (u.get("output_tokens_details") or {}).get("thinking_tokens", 0),
                }
                st = u.get("server_tool_use") or {}
                row["web_search"] = st.get("web_search_requests", 0)
                row["web_fetch"] = st.get("web_fetch_requests", 0)
                for k, v in row.items():
                    totals[k] += v
                    by_model[model][k] += v
                cost[model] += price(model, u)

                # Attribute this turn's marginal input to the tool results that caused it.
                marginal = row["input"] + row["write_5m"] + row["write_1h"]
                if pending and marginal:
                    total_b = sum(n for _, n in pending) or 1
                    assigned = 0
                    for name, n in pending:
                        share = marginal * n // total_b
                        attributed[name] += share
                        assigned += share
                    attributed["(prompt overhead)"] += marginal - assigned
                elif marginal:
                    attributed["(prompt overhead)"] += marginal
                pending = []

            for b in blocks(msg):
                if b.get("type") == "tool_use":
                    tool_of[b.get("id")] = b.get("name", "unknown")
                    calls[b.get("name", "unknown")] += 1

    return {
        "transcript": path, "turns": turns, "totals": dict(totals),
        "by_model": {m: dict(v) for m, v in by_model.items()},
        "cost_usd": dict(cost), "total_usd": sum(cost.values()),
        "calls": dict(calls), "result_bytes": dict(result_bytes),
        "attributed": dict(attributed),
    }


def subagents(path):
    """Cost of each subagent transcript beside this session's transcript."""
    rows = []
    for sub in sorted(glob.glob(os.path.join(path[:-len(".jsonl")], "subagents", "agent-*.jsonl"))):
        meta = {}
        try:
            meta = json.load(open(sub[:-len(".jsonl")] + ".meta.json"))
        except (OSError, json.JSONDecodeError):
            pass
        r = analyse(sub)
        models = sorted(r["by_model"], key=lambda m: -r["cost_usd"].get(m, 0)) or ["unknown"]
        rows.append({"description": meta.get("description", os.path.basename(sub)),
                     "model": models[0], "turns": r["turns"], "usd": r["total_usd"]})
    return rows


def render(r):
    t, out = r["totals"], []
    k = lambda n: f"{n/1000:.1f}k" if n >= 1000 else str(n)
    marginal = t.get("input", 0) + t.get("write_5m", 0) + t.get("write_1h", 0)
    carry = t.get("cache_read", 0)
    gen = t.get("output", 0)

    out.append("### Run cost")
    out.append("")
    subs = r.get("subagents", [])
    sub_usd = sum(x["usd"] for x in subs)
    out.append(f"- total: **~${r['total_usd'] + sub_usd:.2f}** at list price · {r['turns']} model turns · "
               f"{sum(r['calls'].values())} tool calls"
               + (f" · main ${r['total_usd']:.2f} + {len(subs)} subagents ${sub_usd:.2f}" if subs else ""))
    out.append(f"- new context {k(marginal)} · carry (cache re-read) {k(carry)} · generated {k(gen)}"
               + (f" (thinking {k(t['thinking'])})" if t.get("thinking") else ""))
    if t.get("web_search") or t.get("web_fetch"):
        out.append(f"- server tools: {t.get('web_search',0)} web searches, {t.get('web_fetch',0)} web fetches "
                   "(billed per request, not included above)")
    if carry > marginal * 3 and r["turns"] > 10:
        out.append(f"- ⚠️ carry is {carry/max(marginal,1):.1f}x new context — the run is paying mostly to "
                   "re-read itself. Look at turn count and context size, not at the tool table.")
    out.append("")
    out.append("| Tool | Calls | Result bytes | New-context tokens | Share |")
    out.append("|---|---:|---:|---:|---:|")
    for name, tok in sorted(r["attributed"].items(), key=lambda x: -x[1]):
        if not tok:
            continue
        out.append(f"| {name} | {r['calls'].get(name,'—') if name in r['calls'] else '—'} "
                   f"| {k(r['result_bytes'].get(name,0))} | {k(tok)} "
                   f"| {100*tok/max(marginal,1):.0f}% |")
    if subs:
        out.append("")
        out.append("| Subagent | Model | Turns | $ |")
        out.append("|---|---|---:|---:|")
        for x in subs:
            out.append(f"| {x['description']} | {x['model']} | {x['turns']} | {x['usd']:.2f} |")
    out.append("")
    out.append("_List-price estimate computed locally from the session transcript; on a subscription "
               "nothing is billed per token. Carry is not attributed to any tool on purpose — it is the "
               "cost of the conversation's length, not of any one call._")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--transcript")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    path = a.transcript or find_transcript()
    if not path or not os.path.exists(path):
        print("run-cost: no session transcript found — skipping cost block.", file=sys.stderr)
        return 0
    r = analyse(path)
    r["subagents"] = subagents(path)
    print(json.dumps(r, indent=2) if a.json else render(r))
    return 0


if __name__ == "__main__":
    sys.exit(main())
