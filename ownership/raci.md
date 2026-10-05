# RACI — IT Operations

- **ID:** `SOP-020`
- **Title:** Ownership matrix (RACI) for IT processes
- **Owner:** IT Administrator
- **Status:** draft
- **Created:** 2026-10-05
- **Review date:** 2027-10-05
- **Applies to:** All IT operational processes

## Purpose

Names exactly who is Responsible, Accountable, Consulted, and Informed for each core process. If something fails, this chart says who owns the outcome. No diffusion.

**R** = Responsible (does the work). **A** = Accountable (owns the outcome; exactly one per row). **C** = Consulted (input before action). **I** = Informed (told after).

## Matrix

| Process | IT Admin | Hiring Manager | Business Leadership | End User |
|---|---|---|---|---|
| New-hire provisioning | R, A | C | I | I |
| Offboarding / access revocation | R, A | C | I (SEV: involuntary) | — |
| Laptop deployment & imaging | R, A | I | — | C |
| Patch management | R, A | — | I | I |
| Phishing simulations | R, A | C | I | I |
| Incident response (SEV-1/2) | R | C | A | I |
| Backup verification | R, A | — | I | — |
| Access reviews (quarterly) | R | A | I | — |
| Vendor management | R | C | A | — |
| Policy exceptions | R | C | A | I |

## Risk ownership

Accountability for a process includes accountability for its risks:

| Risk | Owner | Outcome if it fails |
|---|---|---|
| Orphaned accounts after termination | IT Admin | Unauthorized access; audit finding |
| Unpatched critical vulnerability | IT Admin | Exploitation; incident response |
| Phishing-driven credential theft | IT Admin (program), User (action) | Account compromise; containment |
| Data loss without recoverable backup | IT Admin | Business interruption; leadership decision on acceptance |
| Excess privilege / role creep | Hiring Manager (A), IT Admin (R) | Audit finding; access review remediation |
| Unapproved software / shadow IT | IT Admin | Security exception or removal |

## Rules

- Exactly one **A** per row. If two people think they're accountable, neither is.
- **A** can delegate **R**, never **A**. You can hand off the work; you can't hand off the ownership.
- Review this chart whenever roles change. A RACI that doesn't match reality is worse than none.
