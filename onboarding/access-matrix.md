# Access Matrix

- **ID:** `SOP-003`
- **Title:** Role-based access matrix
- **Owner:** IT Administrator
- **Status:** draft
- **Created:** 2026-10-05
- **Review date:** 2027-10-05
- **Applies to:** All user provisioning
- **Compliance refs:** PCI DSS 4.0 Req 7 (least privilege); GLBA Safeguards (access controls)

## Purpose

Defines exactly which systems each role gets. Provisioning follows this matrix — if it's not on the matrix, it doesn't get provisioned. Changes to the matrix require manager approval and a review-date update.

## TL;DR

Find the hire's role below. Provision exactly what's listed. Nothing more. Role changes go through the mover process; don't stack old and new access.

## Matrix

| System | Sales | Finance | Service | Sales Mgmt |
|---|---|---|---|---|
| Identity (SSO/MFA) | Yes | Yes | Yes | Yes |
| Email & collaboration | Yes | Yes | Yes | Yes |
| CRM / deal system | Yes | Read | No | Yes |
| DealerTrack (SSO) | Yes | Yes | No | Yes |
| Accounting / finance system | No | Yes | No | Read |
| File shares (department) | Sales | Finance | Service | Mgmt |
| Shared workstations | Yes | No | Yes | No |
| Payment terminal area | No | Yes | Yes | No |
| MDM enrolled device | Yes | Yes | Shared | Yes |
| Admin / elevated rights | No | No | No | No |

**Notes:**
- "Read" = read-only access, no modify/delete.
- "Shared" = shared-workstation profile, no persistent personal device.
- No role gets standing admin rights. Elevation is by request, time-bound, logged.
- Contractors get the matrix for their functional role plus an account expiration date.

## Movers

When someone changes roles: provision the new role's access, **remove** the old role's access. Movers are where privilege creep lives — the new access gets added, the old access stays. Don't let it.

## Verification

Quarterly access reviews compare actual group memberships against this matrix. Deviations get a ticket: either the matrix is wrong (update it) or the access is wrong (remove it).

## Tips & pointers

- The matrix is a living document. When a new system arrives, the first question is "which roles get it" — answer it here before provisioning anyone.
- Keep roles coarse. Four roles with clear boundaries beat twelve with overlapping permissions nobody can audit.
- The service column is the one people get wrong. Payment-adjacent access is not the same as payment-system access. The terminal handles the card data; the staff handle the workflow around it.
