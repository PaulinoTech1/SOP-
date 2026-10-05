# Device Hardening Baseline

- **ID:** `SOP-070`
- **Title:** Endpoint hardening baseline
- **Owner:** IT Administrator
- **Status:** draft
- **Created:** 2026-10-05
- **Review date:** 2027-10-05
- **Applies to:** All company-owned endpoints (laptops, desktops, shared workstations)
- **Compliance refs:** PCI DSS 4.0 Req 2 (secure configurations)

## Purpose

Every device gets the same secure baseline before it touches company data. No snowflakes, no exceptions without a documented risk acceptance.

## TL;DR

Enroll in MDM, apply the compliance policy (encryption on, screen lock ≤ 5 min, OS auto-updates, Defender on), remove local admin, install only approved apps. Verify compliance in the console before handing it over. Shared workstations get the kiosk/session profile instead.

## Scope

Covers initial hardening of new and reimaged devices. Does not cover ongoing patch management (see patching procedure) or server hardening.

## Prerequisites

- Device enrolled in MDM (Intune / Google endpoint management).
- Compliance policy published and tested on a pilot device.

## Procedure

1. Enroll the device in MDM during provisioning (Autopilot / zero-touch where available).
2. Confirm the compliance policy applies:
   - Disk encryption enabled (BitLocker / FileVault).
   - Screen lock at 5 minutes or less, requiring authentication.
   - OS updates automatic; deferral windows per the update ring.
   - Endpoint protection active with real-time scanning.
   - Firewall enabled.
3. Remove local administrator rights. Standard user only.
4. Install approved applications per the role profile. No unapproved software.
5. For shared workstations: apply the shared-session profile (automatic sign-out, no persistent profiles, NFC/badge tap if deployed).
6. Verify in the MDM console: device shows **compliant** before it goes to the user.

**Expected result:** Device is compliant in the console, encrypted, locked down, and has only the software its role needs.

## Verification

- MDM compliance report shows the device as compliant.
- Spot-check: attempt to install unapproved software as the user (should fail); confirm encryption status.

## Rollback

Reimage the device to the baseline. There is no partial rollback — a non-compliant device gets wiped and rebuilt.

## Exceptions

- **Developer/engineering roles** needing elevated access: documented exception with manager approval, time-bound, reviewed quarterly. Elevation does not waive encryption or update requirements.
- **Lab/test devices:** Segregated network, labeled, never holding production data.

## Tips & pointers

- Test every policy change on a pilot device first. A bad compliance policy pushed fleet-wide will lock people out of their own machines.
- The shared-workstation profile is the hardest to get right. Too aggressive and sales can't work; too lax and sessions bleed between users. Tune the timeout with actual users watching, not in a vacuum.
- Document every exception. "Temporary" admin rights have a way of becoming permanent.
