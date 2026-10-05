# SOP Health Monitoring

- **ID:** `SOP-060`
- **Title:** SOP health checks and usage tracking
- **Owner:** IT Administrator
- **Status:** draft
- **Created:** 2026-10-05
- **Review date:** 2027-10-05
- **Applies to:** All SOPs in this repo

## Purpose

Procedures rot. Owners leave, systems change, and documents that nobody reads become fiction. This SOP defines how we measure whether each procedure is healthy: structurally sound, current, and actually used.

## TL;DR

Run `scripts/sop-lint.py` on every commit (CI does it automatically). It checks metadata, review dates, cross-references, and required sections. Separately, update `last exercised` whenever you follow a procedure — anything untouched for 180 days gets flagged as stale. Fix the findings or retire the SOP.

## Scope

Covers automated validation (the linter) and usage tracking (exercise dates). Does not cover the quality of the procedure's content — that's what peer review is for.

## Prerequisites

- Python 3 (stdlib only, no dependencies).
- The linter at `scripts/sop-lint.py`.

## Procedure

### 1. Automated checks (CI)

Every push runs the linter via `.github/workflows/sop-health.yml`:

```
python3 scripts/sop-lint.py --strict
```

In strict mode, warnings fail the build. The check validates:

| Check | What it catches |
|---|---|
| Required metadata | Blank owner, missing review date, no title |
| Status values | Typos like `actve`, invalid lifecycle states |
| Review dates | Active SOPs past their review date |
| Required sections | Procedural SOPs missing TL;DR or tips |
| Cross-references | Links to SOP-XXX IDs that don't exist |
| Retirement fields | Retired SOPs without reason, replacement, or approver |

**Expected result:** Green check or a specific list of findings. Findings get fixed in the same change window, not "later."

### 2. Usage tracking (human)

The linter can't tell you whether anyone actually follows the procedure. For that, each SOP carries an optional metadata field:

```
- **Last exercised:** 2026-10-05
```

Update it whenever the procedure is used for real — an onboarding, an incident, a quarterly review. The linter flags active SOPs untouched for 180+ days as stale. Stale means one of three things:

1. **Nobody needs it.** Retire it (see `workflows/sop-retirement.md`).
2. **People need it but don't know it exists.** Fix discoverability, link it from onboarding.
3. **People need it but aren't following it.** That's a training or culture problem, not a documentation problem. Find out why.

**Expected result:** Every active SOP has a recent exercise date or a conscious explanation for why it doesn't.

### 3. Health review (quarterly)

Once a quarter, the owner reviews the full picture:

1. Run the linter, confirm zero findings.
2. List stale SOPs (180+ days without exercise). Decide: retire, promote, or investigate.
3. Check the retirement log for patterns (are we retiring faster than we're writing?).
4. Confirm every active SOP still has a named owner who still works here.

## Verification

- CI is green on the latest commit.
- No active SOP is past its review date.
- Every stale SOP has a disposition (retired, promoted, or under investigation with a due date).

## Rollback

Not applicable — this is a monitoring procedure.

## Exceptions

There are none. Every SOP is subject to health checks.

## Tips & pointers

- The linter catches structure, not sense. A SOP can pass every check and still be wrong. Pair automated checks with periodic human read-throughs.
- `last exercised` only works if updating it is frictionless. Put it in the procedure's final step: "Update the Last exercised date." If it's a separate chore, nobody will do it.
- Watch for the opposite problem too: an SOP exercised constantly but never updated. High usage with an old review date means the procedure is load-bearing and drifting from reality. That's the most dangerous kind of stale.
- When CI goes red on a docs repo, fix it the same day. A broken health check that everyone ignores teaches the team that health checks don't matter.
