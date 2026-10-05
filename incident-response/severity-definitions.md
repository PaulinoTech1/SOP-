# Severity Definitions

- **ID:** `SOP-010`
- **Title:** Incident severity definitions
- **Owner:** IT Administrator
- **Status:** draft
- **Created:** 2026-10-05
- **Review date:** 2027-10-05
- **Applies to:** All IT incidents

## Purpose

A shared language for how bad it is. Severity drives who gets woken up, how fast we respond, and how we communicate. When in doubt, pick the higher severity. You can always downgrade.

## TL;DR

SEV-1: business is down or data is being stolen. Drop everything. SEV-2: badly degraded or contained security event. Respond within the hour. SEV-3: minor, workaround exists. SEV-4: informational. Unsure? Go one level higher.

## Definitions

### SEV-1 — Critical

- Core business function is down or data is actively being compromised.
- Examples: ransomware in progress, payment terminal outage during business hours, identity provider down, confirmed data breach.
- **Response target:** Immediate. All hands.
- **Communication:** Notify leadership within 30 minutes. Updates every 30 minutes until resolved.

### SEV-2 — Major

- Significant degradation or a security event with contained scope.
- Examples: single site offline, phishing campaign with credential submissions, failed backups for a critical system.
- **Response target:** Within 1 hour.
- **Communication:** Notify management within 1 hour. Updates every 2 hours.

### SEV-3 — Minor

- Limited impact, workaround available.
- Examples: single workstation failure, non-critical application bug, isolated malware blocked by endpoint protection.
- **Response target:** Within 4 business hours.
- **Communication:** Ticket updates. No leadership notification required.

### SEV-4 — Informational

- No impact, or proactive finding.
- Examples: phishing simulation results, vulnerability scan findings, capacity warnings.
- **Response target:** Next business day.
- **Communication:** Ticket or report. Trends reviewed monthly.

## Downgrade / upgrade

Anyone can escalate a severity. Only the incident owner can downgrade, and the reason goes in the ticket. When in doubt, escalate.

## Tips & pointers

- New responders consistently under-severity. If you're debating between two levels, the higher one is almost always right.
- SEV-2s that last more than 4 hours are SEV-1s in practice. Time is a severity multiplier.
- Don't let "we have a workaround" talk you down from SEV-2 to SEV-3 if the workaround requires heroics. A workaround that only one person knows isn't a workaround, it's a risk.
