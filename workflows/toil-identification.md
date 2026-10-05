# Toil Identification

- **ID:** `SOP-040`
- **Title:** Finding and measuring repetitive operational work
- **Owner:** IT Administrator
- **Status:** draft
- **Created:** 2026-10-05
- **Review date:** 2027-10-05
- **Applies to:** All IT operational tasks

## Purpose

SOPs document how work gets done. This procedure identifies which of that work is repetitive enough to automate. The goal isn't documentation for its own sake — it's finding the tasks that eat hours every month so they can be measured, then reduced, then eliminated.

## TL;DR

List everything you do more than twice a month. Score it: frequency × time × error risk. High score + deterministic steps = automate now. Low automatability = document it well and keep it manual. And always ask whether the task should exist before you automate it.

## Scope

Covers identification and scoring of repetitive tasks. Automation implementation is tracked separately per task.

## Prerequisites

- Existing SOPs or runbooks for the processes being evaluated.
- Rough sense of task frequency (tickets, calendar, memory — precision comes later).

## Procedure

### 1. Inventory the work

List every recurring task IT performs. Sources:

- Ticket history (tag repeat issues).
- Calendar (recurring maintenance, reviews, scans).
- The SOPs in this repo (each one is a candidate).
- Ask: "what did I do more than twice this month that followed the same steps?"

Log each in `ownership/toil-register.md`.

### 2. Score each task

Rate 1–5 on each axis:

| Axis | 1 | 5 |
|---|---|---|
| **Frequency** | Quarterly or less | Daily |
| **Manual time** | Under 15 min | Over 2 hours |
| **Error risk** | Mistake is trivial | Mistake causes outage, breach, or audit finding |
| **Automatability** | Requires human judgment throughout | Fully deterministic steps |

**Priority score = Frequency × Manual time × Error risk.** Automatability gates whether it's worth attempting, not whether it matters.

### 3. Classify

- **Automate now** (score ≥ 48, automatability ≥ 4): Build it. Track in the register.
- **Automate next** (score 20–47): Document well, automate when capacity allows.
- **Keep manual** (automatability ≤ 2): Some work needs a human. Document it excellently instead.
- **Eliminate** (low value, any score): Ask whether the task should exist at all before automating it. Automating a pointless task just produces pointless output faster.

### 4. Measure before automating

For anything in "automate now": time it manually three times. Record the average. This is your baseline — without it, you can't prove the automation helped.

### 5. Review quarterly

Re-score the register every quarter. Priorities shift as the environment changes. New hires, new systems, and new compliance requirements all create new toil.

## Verification

The toil register has a scored entry for every recurring task, each "automate now" item has a baseline measurement, and the quarterly review date is on the calendar.

## Rollback

Not applicable — this is an assessment procedure.

## Exceptions

One-off incidents and novel troubleshooting are not toil. Don't try to automate what you haven't seen twice.

## Tips & pointers

- Time the manual task **before** you automate it. Without a baseline, "the script is faster" is a feeling, not a fact.
- Start with the highest error-risk task, not the most frequent one. Automating a 5-minute daily task saves 20 hours a year; automating an error-prone quarterly task prevents the incident that costs a week.
- The `eliminate` column is the most valuable one. Every task you delete is better than every task you automate.
- Re-scoring feels like overhead until the first time a priority shift saves you from automating the wrong thing.
