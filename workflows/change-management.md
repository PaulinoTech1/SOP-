# Change Management

- **ID:** `SOP-074`
- **Title:** Lightweight change management
- **Owner:** IT Administrator
- **Status:** draft
- **Created:** 2026-10-05
- **Review date:** 2027-10-05
- **Applies to:** All production IT changes

## Purpose

Prevent the 2 AM "who changed what" mystery. Every significant change gets proposed, reviewed, tested, and logged — proportional to its risk, not buried in bureaucracy.

## TL;DR

Propose the change (what, why, risk, rollback). Get approval proportional to the risk. Test it somewhere safe first. Do it in the maintenance window. Log what happened. If it breaks, roll back first and diagnose second.

## Scope

Covers changes to production systems, network, security controls, and MDM policies. Does not cover routine operational tasks already documented in SOPs (password resets, new-hire provisioning).

## Prerequisites

- The change is described in writing: what, why, expected impact, rollback plan.
- A test environment or pilot group is available for non-trivial changes.

## Procedure

### 1. Classify the change

| Class | Examples | Approval | Window |
|---|---|---|---|
| **Standard** | Pre-approved, low risk, repeatable (patch Tuesday, cert renewal) | Self-approved, logged | Anytime |
| **Normal** | Config changes, new software deployment, firewall rules | Manager / peer review | Maintenance window |
| **Emergency** | Active incident, critical vulnerability | Verbal approval, documented after | Immediate |

### 2. Propose (Normal and Emergency)

Write it down: what changes, why, what could go wrong, how to undo it. One paragraph is enough for most changes. The rollback plan is mandatory — "we'll figure it out" is not a plan.

### 3. Review and approve

- **Standard:** No review needed, but log it.
- **Normal:** A second person reviews. They check the blast radius and the rollback plan, not the technical elegance.
- **Emergency:** Verbal approval from whoever's available, full write-up within 24 hours.

### 4. Test

Non-trivial changes get tested on a pilot group or in a lab first. MDM policy changes go to a pilot device. Firewall changes get a rule review before apply.

### 5. Implement and log

Make the change in the maintenance window. Log: what, when, who, result. Link the log entry to the ticket.

**Expected result:** Every production change has a written proposal (except standard), an approval, a test record, and a log entry. No mystery changes.

## Verification

- Monthly: sample recent changes, confirm each has the required artifacts.
- After any incident: check whether an unlogged change contributed. If yes, that's a process failure to address.

## Rollback

Every change carries its own rollback plan from step 2. If the change causes an incident, roll back first — root-cause analysis happens after service is restored.

## Exceptions

- **Emergency changes** skip the written proposal but not the 24-hour write-up. The documentation happens after, not never.

## Tips & pointers

- The goal is preventing surprises, not preventing change. If the process feels like it's slowing everything down, the classification thresholds are wrong — adjust them, don't bypass the process.
- MDM policy changes are the silent killers. A bad compliance policy doesn't throw an error, it just starts locking people out. Always pilot, always have a rollback (previous policy version exported and ready).
- Keep a change calendar visible to the team. Half of "unexpected" outages are changes someone didn't know about.
- Standard changes should be the majority over time. If everything is Normal or Emergency, that's a sign the environment needs more automation and pre-approval, not more meetings.
