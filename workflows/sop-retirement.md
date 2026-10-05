# SOP Retirement

- **ID:** `SOP-050`
- **Title:** Retiring a standard operating procedure
- **Owner:** IT Administrator
- **Status:** draft
- **Created:** 2026-10-05
- **Review date:** 2027-10-05
- **Applies to:** All SOPs in this repo

## Purpose

Defines how an SOP leaves active service. Retirement is a deliberate, recorded event — never a silent deletion. Past audits, control mappings, and incident reviews reference these documents; removing one destroys the evidence chain.

## TL;DR

To retire an SOP: record why it's going, what replaces it (or that nothing does), and who approved it. Mark the file `status: retired`, fill in the retirement fields, add it to the retirement log. Never delete the file.

## Scope

Covers retirement of any SOP in this repository. Does not cover temporary suspension (use `status: expired` and fix it).

## Prerequisites

- The decision to retire, with a reason in one of the categories below.
- If the procedure is being replaced, the replacement SOP exists and is active.

## Retirement reasons

| Reason | Meaning |
|---|---|
| `superseded` | A newer SOP covers this work. Point to the replacement. |
| `eliminated` | The task itself no longer exists (automated away, system decommissioned). |
| `merged` | Folded into another SOP. Point to the surviving document. |
| `obsolete` | The environment changed and the procedure no longer applies. No direct replacement. |

## Procedure

1. Update the SOP's metadata block:
   - `Status:` → `retired`
   - Add `Retired date:`
   - Add `Retirement reason:` (one of the categories above)
   - Add `Replaced by:` (SOP ID, or `none`)
   - Add `Retirement approved by:` (name/role)
2. Add a `## Retirement note` section at the top of the document body explaining in plain language why it was retired and where to go instead.
3. Add an entry to `ownership/retirement-log.md`.
4. Check for references: search the repo for links to this SOP (control mappings, other procedures, the toil register). Update each to point at the replacement or note the retirement.
5. Commit with the message `Retire SOP-XXX: <reason>`.

**Expected result:** The file still exists, is clearly marked retired, explains why, and every reference to it resolves.

## Verification

- The SOP file is present and marked `retired` with all retirement fields filled.
- The retirement log has a matching entry.
- No active document links to the retired SOP without acknowledging the retirement.

## Rollback

Un-retire by reversing the metadata, removing the retirement note, updating the log, and re-entering the normal lifecycle at `draft` for re-review. Retirement is reversible; deletion is not — which is why we don't delete.

## Exceptions

There are none. Every retirement follows this procedure.

## Tips & pointers

- The most common retirement reason over time should be `eliminated`. If nothing is ever eliminated, the toil register isn't doing its job.
- When a system is decommissioned, retire its SOPs in the same change window. Orphaned procedures for dead systems are how new hires get confused.
- The retirement log is an audit asset. It proves the organization deliberately manages its procedures instead of letting them rot.
- If you're tempted to just delete the file because "nobody uses it" — that's exactly the retirement that needs documenting. Future you won't remember why it's gone.
