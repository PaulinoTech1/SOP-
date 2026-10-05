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

## TL;DR

L1 (you) triages everything. Can't fix it in the response window or the scope is growing? Escalate. One owner, one channel, no side threads. SEV-1: tell leadership in 30 min. After it's over: blameless review within 5 days, action items with owners.

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

## Tips & pointers

- Declare the incident early. "I think this might be a SEV-2" costs nothing; discovering it was a SEV-1 three hours later costs everything.
- Write the timeline **during** the incident, not after. Memory degrades fast and the review is only as good as the timeline.
- The hardest escalation is the first one. If you're unsure whether to wake someone up, wake them up. They'll forgive a false alarm faster than a late one.
- Keep a printed copy of the severity definitions where you work. You won't want to go looking for a wiki page at 2 AM.
