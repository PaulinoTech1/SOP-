# Offboarding Checklist

- **ID:** `SOP-002`
- **Title:** Employee offboarding — access revocation and asset recovery
- **Owner:** IT Administrator
- **Status:** draft
- **Created:** 2026-10-05
- **Review date:** 2027-10-05
- **Applies to:** All departing employees and contractors, all sites
- **Compliance refs:** PCI DSS 4.0 Req 8 (revoke access immediately upon termination); GLBA Safeguards (access controls)

## Purpose

Remove a departing person's access completely and promptly, recover company assets, and preserve any data the business needs to retain. Terminations are time-sensitive; this procedure has explicit time targets.

## TL;DR

Block sign-in and kill all sessions within 1 hour. Strip group memberships within 4 hours. Collect the hardware within 2 business days. Don't delete the account for 30 days (retention + license recovery). Involuntary terms: do steps 1–2 before the person is notified.

## Scope

Covers account disablement, access revocation, device recovery, and data handling. Does not cover HR exit interviews or final pay.

## Prerequisites

- Termination notice with effective date and time, and classification: voluntary, involuntary, or contractor end-of-term.
- Manager confirms which shared resources (mailboxes, files) need retention or transfer.

## Procedure

### 1. Immediate actions (within 1 hour of effective time)

1. Block sign-in on the identity provider. Do not delete the account yet.
2. Revoke all active sessions and refresh tokens.
3. Disable VPN and remote-access credentials.
4. If involuntary: change passwords on any shared credentials the person knew.

**Expected result:** The person cannot authenticate to anything. Verify by attempting a sign-in.

### 2. Access revocation (within 4 hours)

1. Remove all group memberships and role assignments.
2. Revoke application-specific access (DealerTrack, CRM, accounting, file shares).
3. Transfer mailbox/file ownership per manager direction and retention policy.
4. Deprovision MFA registrations.

**Expected result:** Account exists but has zero effective access.

### 3. Device and asset recovery (within 2 business days)

1. Collect laptop, mobile devices, tokens, and keys. Record return in the asset log.
2. For shared workstations: remove the user's profile and revoke any badge/NFC token bindings.
3. Wipe or reimage returned devices before reassignment.
4. If a device is not returned, escalate per the asset-recovery process and document.

**Expected result:** Every assigned asset is accounted for or escalated.

### 4. Account cleanup (after 30 days, or per retention policy)

1. Convert mailbox to shared or export per retention requirements, then remove the license.
2. Archive OneDrive / drive data per policy, then delete.
3. Delete the identity-provider account after the retention window closes.

**Expected result:** No orphaned accounts remain. License recovered.

## Verification

- Access review: query the identity provider for the disabled account and confirm zero group memberships and zero active sessions.
- Asset log shows every assigned item returned or escalated.

## Rollback

Offboarding is not rolled back. If a termination is rescinded, treat the person as a rehire and follow `new-hire-checklist.md`.

## Exceptions

- **Involuntary terminations:** Steps 1 and 2 happen before the person is notified, coordinated with HR/management. No exceptions to the 1-hour target.
- **Contractors:** Account expiration should already be set at hire. This procedure is the backstop if it wasn't.

## Tips & pointers

- **Verify the block.** After disabling sign-in, actually try to sign in as the user. Trust the console, then confirm it.
- Shared credentials are the silent killer. Keep a list of every shared password the person could know; rotate them on involuntary terms even if you think they never used them.
- The 30-day hold isn't bureaucracy, it's your safety net. Managers always remember the critical file three weeks later.
- Automate this. The JML leaver workflow exists because humans forget steps under time pressure, and offboarding is always under time pressure.
