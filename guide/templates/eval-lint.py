#!/usr/bin/env python3
"""Contract lint. Deterministic, free, no model.

Checks contract.json against skills/*/SKILL.md so a skill can't quietly start
reading or writing a store nobody planned.

Setup: copy contract.json to the repo root and this file to scripts/eval-lint.py.

    python3 scripts/eval-lint.py          # exits 1 on any failure
    python3 scripts/eval-lint.py --quiet  # failures only
"""

import re, sys, json, pathlib, argparse

ROOT = pathlib.Path(__file__).resolve().parent.parent
FAIL, WARN = [], []


def fail(msg): FAIL.append(msg)
def warn(msg): WARN.append(msg)


def check_contract():
    p = ROOT / "contract.json"
    if not p.exists():
        fail("contract.json is missing")
        return
    c = json.loads(p.read_text(encoding="utf-8"))
    stores, skills = c["stores"], c["skills"]
    units = {**skills, **c.get("routines", {})}

    dirs = {d.name for d in (ROOT / "skills").iterdir() if (d / "SKILL.md").exists()}
    for name in sorted(dirs - set(skills)):
        fail(f"skill '{name}' has no entry in contract.json")
    for name in sorted(set(skills) - dirs):
        fail(f"contract.json lists skill '{name}' but no SKILL.md exists")

    for sid, st in stores.items():
        for path in st.get("paths", []):
            if not (ROOT / path).exists():
                fail(f"store '{sid}': path {path} does not exist")

    live = {n: u for n, u in units.items() if u.get("trigger") != "retired"}
    for n, u in live.items():
        for sid in u.get("reads", []) + u.get("writes", []):
            if sid not in stores:
                fail(f"'{n}' references unknown store '{sid}'")

    for sid, st in stores.items():
        if st.get("terminal"):
            continue
        writers = [n for n, u in live.items() if sid in u.get("writes", [])]
        readers = [n for n, u in live.items() if sid in u.get("reads", [])]
        if not writers and not st.get("external") and not st.get("human"):
            fail(f"store '{sid}' is read but nothing writes it")
        if not readers:
            warn(f"store '{sid}' is written but nothing reads it")

    # drift guard: a path a SKILL.md names must be in that skill's reads or writes
    for n, u in skills.items():
        if u.get("trigger") == "retired":
            continue
        f = ROOT / "skills" / n / "SKILL.md"
        text = f.read_text(encoding="utf-8") if f.exists() else ""
        declared = set(u.get("reads", [])) | set(u.get("writes", []))
        for sid, st in stores.items():
            if sid in declared:
                continue
            for path in st.get("paths", []):
                pat = re.escape(path) + ("/" if "." not in path else r"(?![\w-])")
                if re.search(pat, text):
                    warn(f"{n}/SKILL.md mentions {path} but contract.json does not list store '{sid}' for it")
                    break


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()
    check_contract()
    if not args.quiet:
        for m in WARN:
            print(f"warn  {m}")
    for m in FAIL:
        print(f"FAIL  {m}")
    if FAIL:
        print(f"\n{len(FAIL)} failure(s), {len(WARN)} warning(s).")
        return 1
    if not args.quiet:
        print(f"ok — contract holds ({len(WARN)} warning(s)).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
