#!/usr/bin/env python3
"""SOP health check — CI for procedures.

Walks the repo, validates every SOP against the template standard, and
reports health per document plus a repo-wide summary.

Checks:
  - Required metadata fields present (ID, Title, Owner, Status, Created, Review date)
  - Status is a known value
  - Active SOPs are not past their review date
  - Procedural SOPs have TL;DR and Tips & pointers sections
  - SOP-XXX cross-references resolve to a real document
  - Retired SOPs carry retirement fields

Usage:
  python3 scripts/sop-lint.py [--strict]

Exit code 0 = all checks pass, 1 = findings (details on stdout).
In --strict mode, warnings become failures.
"""

import os
import re
import sys
from datetime import date, datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
VALID_STATUSES = {"draft", "active", "expired", "retired"}
RETIREMENT_REASONS = {"superseded", "eliminated", "merged", "obsolete"}
# Directories whose docs are procedures (need TL;DR + tips), vs reference docs.
PROCEDURE_DIRS = {"onboarding", "workflows", "incident-response"}
SKIP_FILES = {"README.md"}

META_RE = re.compile(r"^- \*\*(.+?):\*\*\s*(.*)$")
SOPREF_RE = re.compile(r"SOP-(\d{3})")


def parse_metadata(text):
    meta = {}
    for line in text.splitlines():
        m = META_RE.match(line.strip())
        if m:
            meta[m.group(1).strip().lower()] = m.group(2).strip().strip("`")
    return meta


def find_sops():
    sops = {}
    for md in sorted(REPO.rglob("*.md")):
        rel = md.relative_to(REPO)
        if rel.name in SKIP_FILES:
            continue
        if ".github" in rel.parts:
            continue
        if rel.parts[0] == "templates":
            continue  # the blank template is not a real SOP
        text = md.read_text(encoding="utf-8")
        meta = parse_metadata(text)
        if "id" in meta:
            sops[meta["id"]] = (rel, text, meta)
    return sops


def check_sop(sop_id, rel, text, meta, all_ids):
    findings = []  # (level, message)
    is_procedure = rel.parts[0] in PROCEDURE_DIRS

    for field in ("id", "title", "owner", "status", "created", "review date"):
        if not meta.get(field):
            findings.append(("error", f"missing required field: {field}"))

    status = meta.get("status", "")
    if status and status not in VALID_STATUSES:
        findings.append(("error", f"unknown status '{status}'"))

    review = meta.get("review date", "")
    if review:
        try:
            review_d = datetime.strptime(review, "%Y-%m-%d").date()
            if review_d < date.today() and status == "active":
                findings.append(("error", f"review date {review} is past (status is active)"))
            elif review_d < date.today():
                findings.append(("warning", f"review date {review} is past"))
        except ValueError:
            findings.append(("warning", f"review date '{review}' is not YYYY-MM-DD"))

    if is_procedure:
        if "## TL;DR" not in text:
            findings.append(("warning", "procedural SOP missing TL;DR section"))
        if "## Tips & pointers" not in text:
            findings.append(("warning", "procedural SOP missing Tips & pointers section"))

    for ref in set(SOPREF_RE.findall(text)):
        ref_id = f"SOP-{ref}"
        if ref_id != sop_id and ref_id not in all_ids:
            findings.append(("warning", f"dangling reference to {ref_id}"))

    if status == "retired":
        for field in ("retired date", "retirement reason", "replaced by", "retirement approved by"):
            if not meta.get(field):
                findings.append(("error", f"retired SOP missing field: {field}"))
        reason = meta.get("retirement reason", "")
        if reason and reason not in RETIREMENT_REASONS:
            findings.append(("error", f"unknown retirement reason '{reason}'"))

    exercised = meta.get("last exercised", "")
    if exercised:
        try:
            ex_d = datetime.strptime(exercised, "%Y-%m-%d").date()
            if (date.today() - ex_d).days > 180 and status == "active":
                findings.append(("warning", f"not exercised in 180+ days ({exercised}) — stale?"))
        except ValueError:
            findings.append(("warning", f"last exercised '{exercised}' is not YYYY-MM-DD"))

    return findings


def main():
    strict = "--strict" in sys.argv
    sops = find_sops()
    all_ids = set(sops)
    total_errors = 0
    total_warnings = 0

    print(f"SOP health check — {len(sops)} documents\n")
    for sop_id in sorted(all_ids):
        rel, text, meta = sops[sop_id]
        findings = check_sop(sop_id, rel, text, meta, all_ids)
        errors = [f for f in findings if f[0] == "error"]
        warnings = [f for f in findings if f[0] == "warning"]
        total_errors += len(errors)
        total_warnings += len(warnings)
        if findings:
            print(f"{sop_id} ({rel})")
            for level, msg in findings:
                print(f"  [{level}] {msg}")
        else:
            print(f"{sop_id} ({rel}) — OK")

    print(f"\n{len(sops)} documents, {total_errors} errors, {total_warnings} warnings")
    fail_on = total_errors + (total_warnings if strict else 0)
    sys.exit(1 if fail_on else 0)


if __name__ == "__main__":
    main()
