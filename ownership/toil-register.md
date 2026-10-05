# Toil Register

- **ID:** `SOP-041`
- **Title:** Repetitive task inventory and automation pipeline
- **Owner:** IT Administrator
- **Status:** draft
- **Created:** 2026-10-05
- **Review date:** 2027-01-05
- **Applies to:** All IT operational tasks

## Purpose

The working inventory of repetitive tasks, their cost, and where each sits in the automation pipeline. This is the growth engine of the SOP practice: every entry here is either hours reclaimed or a conscious decision to keep doing it by hand.

Scoring method: see `workflows/toil-identification.md`. Priority = Frequency × Manual time × Error risk (each 1–5).

## Pipeline stages

`identified` → `measured` → `automated` → `eliminated`
(or `accepted` for work that stays manual by decision)

## Register

| Task | Freq | Time | Risk | Auto | Priority | Stage | Notes |
|---|---|---|---|---|---|---|---|
| New-hire account provisioning | 4 | 3 | 4 | 5 | 48 | automated | JML scripts; dry-run by default, mutation gate |
| Offboarding access revocation | 4 | 3 | 5 | 5 | 60 | automated | JML leaver workflow; 1-hr target for involuntary |
| Quarterly access reviews | 2 | 4 | 4 | 4 | 32 | measured | Read-only review script exists; scheduling is manual |
| Phishing simulation setup & reporting | 2 | 3 | 2 | 4 | 12 | identified | GoPhish; campaign setup is repeatable |
| Device provisioning & enrollment | 3 | 3 | 3 | 4 | 27 | identified | Intune Autopilot is the target state |
| Password / MFA resets | 5 | 1 | 2 | 3 | 10 | accepted | SSPR covers most; remainder needs a human anyway |
| Quarterly vulnerability scans | 2 | 2 | 4 | 4 | 16 | identified | ASV scans; scheduling + report collection is manual |
| License reconciliation | 2 | 3 | 3 | 4 | 18 | identified | M365 / Google Workspace true-ups |
| Shared-workstation profile resets | 3 | 2 | 2 | 3 | 12 | identified | Tied to NFC/session lifecycle |
| New-hire Day-1 verification | 4 | 1 | 3 | 2 | 12 | accepted | Human contact matters here; keep manual |

## Growth opportunities (next 12 months)

1. **Access reviews → automated.** The review script exists; what's manual is the scheduling, manager follow-up, and evidence collection. Automating the workflow around the script reclaims the most hours per quarter.
2. **Device provisioning → Autopilot.** Every manual imaging session is toil. Zero-touch enrollment moves this from `identified` to `eliminated`.
3. **Vulnerability scans → scheduled pipeline.** Scans run on a schedule; report collection and ticket creation shouldn't need a human to kick them off.

## Rules

- Every `automated` entry links to the code or system that does it.
- Every `accepted` entry has a reason. "We've always done it this way" is not a reason.
- Re-score quarterly. A task's priority changes as the environment changes.
