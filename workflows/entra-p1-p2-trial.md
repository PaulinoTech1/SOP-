# Entra ID P1/P2 License Trial — Evaluation and Gated Rollout

- **ID:** `SOP-075`
- **Title:** Entra ID P1/P2 license trial evaluation
- **Owner:** IT Administrator
- **Status:** draft
- **Created:** 2026-10-06
- **Review date:** 2027-10-06
- **Applies to:** Microsoft Entra ID tenant, Intune, break-glass admin accounts, pilot user group
- **Compliance refs:** PCI DSS 4.0 Req 7 (least privilege), Req 8 (MFA / authentication); GLBA Safeguards (access controls, authentication)
- **Last exercised:** 2026-10-06

## Purpose

Run a time-boxed Entra ID P1/P2 free trial to unlock and validate the identity controls the base Intune license cannot provide (Conditional Access, role-assignable groups, Privileged Identity Management, automatic MDM enrollment), in the correct order, without ever leaving the tenant without MFA. This procedure exists because several intended controls are license-gated, and turning the wrong one on in the wrong order can lock everyone out or strip MFA from the whole tenant.

## TL;DR

Start the P2 trial (P2 includes P1), assign licenses to the admins and pilot users, then build the gated controls in order: role-assignable groups → directory role assignments → a verified require-MFA Conditional Access policy with break-glass excluded → the rest of the CA baseline → and only then disable Security Defaults. Test break-glass sign-in before you trust any of it. Trials expire in 30 days — decide to buy or revert, and re-enable Security Defaults before the trial lapses if you revert, or the tenant loses MFA.

## Scope

Covers evaluating Entra ID P1/P2 under a free trial and the ordered rollout of the features it unlocks. Covers the hand-off from the license-independent baseline (groups, break-glass accounts, Intune compliance/config, Windows Update rings) already in place.

Out of scope: the license-independent build itself (done without a trial), day-to-day CA policy tuning, and PIM operational use after initial setup (those get their own procedures once the licensing is permanent).

## Prerequisites

- Global Administrator access, and two cloud-only break-glass Global Admin accounts that already exist and are excluded from any future CA policy.
- Security Defaults currently **enabled** (the tenant's only MFA enforcement until CA is ready).
- The license-independent baseline already applied and verified: security groups, Intune device compliance policy, BitLocker/encryption configuration, Windows Update ring, Enrollment Status Page.
- A written rollback plan and a maintenance window (see `workflows/change-management.md`, SOP-074 — this is a Normal change).
- A decision owner for the buy-vs-revert call before the trial expires.

## Procedure

### 1. Record the starting state

Capture current licensing (the base SKU), the Security Defaults state (enabled), and the list of groups whose role-assignable flag is still pending. This is the evidence baseline you compare against after the trial.

### 2. Start the trial

In the Microsoft 365 admin center (Billing → Purchase services) or the Microsoft Entra admin center, start the free trial of **Microsoft Entra ID P2** (it includes all P1 features) or the equivalent Enterprise Mobility + Security E5 trial. Trials are typically 30 days with a fixed seat count. Note the activation date and the expiry date in the change log immediately.

### 3. Assign licenses

A trial SKU does nothing until it is assigned. Assign P1/P2 licenses to the admin accounts and the pilot user group. Gated features only evaluate for licensed users; an unlicensed user is not protected by a CA policy and cannot be PIM-eligible.

### 4. Create role-assignable groups

Create the admin role-assignable groups with `isAssignableToRole = true`. This flag is **immutable** — it can only be set at creation and never changed afterward — which is exactly why these groups were deferred out of the license-independent phase rather than created wrong. Expected result: the groups exist and are role-assignable.

### 5. Assign directory roles

Assign the appropriate built-in directory roles to those groups (or, with P2, make the assignments eligible via PIM in the next step rather than permanent). Keep Global Administrator assignments minimal; everything else gets least-privilege roles.

### 6. Build and VERIFY a require-MFA Conditional Access policy

Create a Conditional Access policy that requires MFA for all users, with the break-glass accounts **excluded**. Enable it and verify it actually prompts for MFA with a normal test user, and verify a break-glass account can still sign in without being blocked. Do not proceed until both are confirmed. This policy is the safety net that replaces Security Defaults.

### 7. Add the rest of the CA baseline

Add the supporting policies (block legacy authentication; require a compliant device, moved from report-only to enabled once validated). Keep break-glass exclusions on every policy.

### 8. Disable Security Defaults — only now

With a verified require-MFA CA policy in place and break-glass sign-in tested, disable Security Defaults. Doing this before step 6 is verified would leave the tenant with no MFA. Re-test a normal sign-in (should still be prompted for MFA via CA) and a break-glass sign-in (should still work).

### 9. Configure PIM (P2)

Convert standing privileged role assignments to eligible, just-in-time activation with approval and justification. Set activation duration and reviewers. This is the main reason to trial P2 over P1.

### 10. Enable the remaining P1-gated features

Dynamic group membership, group-based licensing, and **automatic MDM enrollment (Windows Autopilot)**. The Autopilot deployment profile and the already-created Enrollment Status Page start working once automatic enrollment is available under P1.

**Expected result:** every gated control is live and verified, Security Defaults is off only because a tested CA require-MFA policy replaced it, and break-glass access has been proven to still work.

## Verification

- A normal licensed user is prompted for MFA by the CA policy (not by Security Defaults).
- Both break-glass accounts can sign in and are excluded from every CA policy.
- Role-assignable groups show `isAssignableToRole = true` and carry their intended directory roles.
- PIM shows the privileged roles as eligible, not permanent.
- Autopilot + ESP evaluate on a pilot device.
- Evidence captured: licensing before/after, the CA policy objects, the Security Defaults state change, and the Microsoft-authored audit records for each change.

## Rollback

The trial is time-boxed (30 days). Before it expires, the decision owner either purchases the licenses or reverts. **If reverting:** re-enable Security Defaults first (so MFA is not lost), then stop relying on CA policies — when P1 lapses, CA stops being enforced, and a tenant with Security Defaults off and no P1 has no MFA at all. Role-assignable groups created under the trial persist, but their role assignments cannot be managed without P1; document them so they are not mistaken for active controls. Any single step rolls back by disabling the policy or configuration it created; the one-way door is disabling Security Defaults, which is why step 8 is gated behind a verified CA policy.

## Exceptions

- **No pilot users licensed yet:** you can still create role-assignable groups and CA policies, but you cannot verify MFA enforcement without at least one licensed non-admin test user. Do not disable Security Defaults until that verification is done.
- **Lab / test tenant with no real data:** the same order still applies, because the failure mode (locking out the only admin) is identical. Break-glass accounts are the mitigation regardless of data sensitivity.

## Results — lab evaluation (2026-10-06)

Validated in a test tenant that held the base Intune SKU only (no Entra ID P1/P2) with Security Defaults enabled. Findings:

**Confirmed license-independent (done without any trial):** security groups, two cloud-only break-glass Global Admin accounts, Intune device compliance policy, BitLocker/endpoint-protection device configuration, a Windows Update for Business ring, and an Enrollment Status Page. All created and assigned successfully on the base license.

**Confirmed to require Entra ID P1:** Conditional Access policies; role-assignable groups (`isAssignableToRole = true`); dynamic group membership; group-based licensing; and automatic MDM enrollment — which is why the **Windows Autopilot deployment profile could not be created** on the base license. The Autopilot API returned an opaque backend error for every request shape, while the Enrollment Status Page (same API path) succeeded, isolating the cause to the missing automatic-enrollment entitlement rather than permissions. Autopilot was therefore re-scoped from "license-independent" to P1-gated.

**Confirmed to require Entra ID P2:** Privileged Identity Management (eligible / just-in-time roles), access reviews, and risk-based (Identity Protection) Conditional Access.

**Sequencing lesson:** the original apply order disabled Security Defaults before Conditional Access existed, and the CA baseline had no require-MFA policy. On an unlicensed tenant that ordering would have removed all MFA. The corrected order (this SOP) never disables Security Defaults until a verified require-MFA CA policy with break-glass exclusions is in place.

## Tips & pointers

- The immutable `isAssignableToRole` flag is the trap. If you create the admin groups during the license-independent phase to "save time," they come out non-role-assignable and you cannot fix them — you have to delete and recreate under P1. Wait for the trial.
- A trial SKU assigned to nobody protects nobody. The most common "my CA policy isn't working" cause is an unlicensed target user.
- Disabling Security Defaults is the only genuinely dangerous step. Treat step 8 as a one-way door: verified CA policy first, break-glass sign-in tested, then flip it — never the reverse.
- Set a calendar reminder for day 25 of a 30-day trial. The dangerous state is a lapsed trial with Security Defaults already off and nobody watching.
- Keep break-glass excluded from every CA policy, every time. The whole point is an account that still works when a policy misfires.
- Copy `templates/sop-template.md` if you spin a dedicated PIM or Conditional Access operational SOP out of step 9 later; this document is the trial/rollout, not the steady-state operation.

## Change log

| Date | Author | Change |
|---|---|---|
| 2026-10-06 | IT Administrator | Initial draft; lab-validated license gating and corrected rollout order. |
