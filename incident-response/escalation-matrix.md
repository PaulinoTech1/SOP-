# Escalation Matrix

- **ID:** `SOP-011`
- **Title:** Incident escalation protocol
- **Owner:** IT Administrator
- **Status:** draft
- **Created:** 2026-10-05
- **Review date:** 2027-10-05
- **Applies to:** All IT incidents, all sites

## Purpose

Defines who gets involved at each severity, in what order, and what each level is expected to do. No guessing during an incident.

## Escalation levels

| Level | Role | Engaged at | Responsibility |
|---|---|---|---|
| L1 | IT Administrator (on-call) | All incidents | Triage, contain, resolve or escalate. Owns the ticket. |
| L2 | IT Manager / senior tech | SEV-2 and above, or L1 requests help | Technical direction, vendor escalation, resource decisions. |
| L3 | Business leadership | SEV-1, or SEV-2 lasting > 4 hours | Business continuity decisions, customer/staff communication, spend approval. |
| L4 | External | SEV-1 with suspected breach, or as required | Incident-response retainer, legal counsel, law enforcement, payment processor. |

## Escalation triggers

Escalate to the next level when any of these are true:

- The current level cannot contain or resolve within the severity's response target.
- The scope expands (more systems, more users, more sites affected).
- There is any indication of data compromise or regulatory notification obligation.
- The incident owner requests it. No justification required.

## Communication rules

- **One incident owner.** The owner coordinates; everyone else executes. Ownership transfers explicitly, never by assumption.
- **One channel.** All incident coordination happens in the designated channel/ticket. No side threads.
- **Status updates** follow the severity definitions. "No update" is never the update; report what you know and what you're doing next.
- **No speculation externally.** Only the designated communicator (L3 or their delegate) speaks to customers, staff-wide, or press.

## Post-incident

Every SEV-1 and SEV-2 gets a blameless post-incident review within 5 business days:

1. Timeline of what happened.
2. What went well.
3. What didn't.
4. Action items with owners and due dates.

The review is about the system, not the person. If people fear the review, they'll hide the next incident.
