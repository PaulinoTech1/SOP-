# New-Hire Onboarding Checklist

- **ID:** `SOP-001`
- **Title:** Employee onboarding — accounts, devices, access
- **Owner:** IT Administrator
- **Status:** draft
- **Created:** 2026-10-05
- **Review date:** 2027-10-05
- **Applies to:** All new hires, all sites
- **Compliance refs:** PCI DSS 4.0 Req 7 (least privilege), Req 8 (identification/authentication); GLBA Safeguards (access controls)

## Purpose

Provision a new employee with exactly the access their role requires, on a compliant device, with a verifiable trail. No more, no less.

## Scope

Covers account creation, device assignment, application access, and Day-1 verification. Does not cover HR paperwork, payroll, or physical building access (facilities).

## Prerequisites

- Signed offer with start date, role, department, and manager.
- Manager has confirmed the access profile for the role (see `access-matrix.md`).
- Device available from inventory or procurement.

## Procedure

### 1. Create identity (Day -3 to Day -1)

1. Create user in the identity provider (Entra ID / Google Workspace per role).
2. Assign to role-based groups only. No individual permission grants.
3. Enforce MFA enrollment at first sign-in.
4. Set account to require password change at first logon if not using SSO-only.

**Expected result:** Account exists, disabled or blocked from sign-in until start date.

### 2. Provision device (Day -2 to Day -1)

1. Assign device from inventory; record asset tag, serial, and assignee.
2. Enroll in device management (Intune / Google endpoint management).
3. Verify compliance policies apply: disk encryption, screen lock, OS updates.
4. Install role-required applications only.

**Expected result:** Device enrolled, compliant, and showing in management console.

### 3. Grant application access (Day -1)

1. Provision per the access matrix for the hire's role:
   - **Sales:** DealerTrack SSO, shared-workstation profile, CRM.
   - **Finance:** Accounting system, least-privilege file shares.
   - **Service:** Payment-terminal area access (no card-data system access beyond the terminal itself).
2. Confirm no standing admin rights. Elevate only via request with manager approval.

**Expected result:** User can reach every system on their role profile, nothing else.

### 4. Day-1 verification

1. Confirm the hire can sign in to their device and primary applications.
2. Walk through MFA setup if not completed.
3. Confirm they received and acknowledged the acceptable-use policy.
4. Enable sign-in (if it was blocked pre-start).

**Expected result:** Hire is productive within the first hour. Any failure is a ticket, not a shrug.

## Verification

- Spot-check: sign in as the user flow (or have them demonstrate) for each provisioned system.
- Audit log shows account creation, group assignments, and device enrollment with timestamps.

## Rollback

If the hire does not start: disable the account, revoke all group memberships, return the device to inventory, and retain the audit trail.

## Exceptions

- **Contractors/temps:** Same checklist, but accounts get an expiration date at creation. No exceptions.
- **Rehires:** Treat as new hire. Do not reactivate the old account; create fresh and re-provision.
