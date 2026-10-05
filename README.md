# SOP

Standard Operating Procedures for IT operations: onboarding, compliance, workflows, incident response, and ownership.

Built to make onboarding faster and operations repeatable. Every procedure follows the same template, has a named owner, and carries a review date. If it doesn't have an owner and a review date, it's a draft, not a procedure.

## Layout

| Directory | Purpose |
|---|---|
| `templates/` | Blank templates. Start here when writing a new SOP. |
| `onboarding/` | Start-here path, access matrix, new-hire and offboarding checklists. |
| `compliance/` | Control mappings for PCI DSS, GLBA, and other frameworks. |
| `workflows/` | Step-by-step operational procedures (provisioning, patching, reviews). Includes the toil-identification process. |
| `incident-response/` | Severity definitions, escalation matrix, response playbooks. |
| `ownership/` | RACI charts, risk register, toil register, retirement log. |
| `scripts/` | The SOP linter (CI for procedures). |

## Reading this repo

New here? Start with `onboarding/start-here.md` — a 45-minute reading path in order.

Want the reasoning behind the design? Read `BUILD.md` — every major decision is recorded as an architecture decision.

Prefer a website to raw Markdown? `mkdocs.yml` builds a searchable docs site (`mkdocs build`, deploy to GitHub Pages).

## Maturity model

SOPs are not the end state. They are the raw material. Each procedure moves through these stages:

1. **Ad-hoc** — done from memory, differently each time.
2. **Documented** — written down, owned, review-dated. (This repo.)
3. **Measured** — timed, scored for toil. You know what it costs.
4. **Automated** — the machine does it; the SOP describes the automation and its guardrails.
5. **Eliminated** — the task no longer needs to exist.

The `ownership/toil-register.md` tracks where every recurring task sits on this ladder. Growth is moving tasks right, not adding more procedures.

## SOP lifecycle

1. **Draft** — written from the template, marked `status: draft`.
2. **Review** — a second person walks through it against the real environment.
3. **Approve** — the owner signs off, sets `review-date` (max 12 months out).
4. **Publish** — `status: active`. This is the version people follow.
5. **Review** — on or before `review-date`, the owner re-validates or retires it.
6. **Retire** — per `workflows/sop-retirement.md`. Marked `retired` with a reason, a replacement pointer, and a log entry. Never deleted, never silent.

A procedure past its review date is **expired**, not active. Expired procedures get fixed or archived, never followed blindly.

## Writing a new SOP

1. Copy `templates/sop-template.md`.
2. Fill in every metadata field. No blank owners, no blank review dates.
3. Write for the person doing the job at 2 AM, not for an auditor.
4. Get it reviewed before marking it active.

## Principles

- **Procedures describe the work, not the aspiration.** If the team doesn't actually do it this way, fix the procedure or fix the work, then document the truth.
- **One owner per procedure.** Shared ownership is no ownership.
- **Compliance mappings reference procedures, not the other way around.** The control mapping in `compliance/` points at the workflow that satisfies it.
