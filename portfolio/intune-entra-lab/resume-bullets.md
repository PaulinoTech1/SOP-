# Resume and interview material: Intune / Entra ID security lab

Companion to the [case study](README.md). All figures come from the same sanitized lab; no tenant identifiers are included.

## Resume bullets

- Built a Microsoft Intune and Entra ID security baseline from scratch in a test tenant: Conditional Access MFA, BitLocker compliance, Windows Update for Business rings, and an Enrollment Status Page, all applied through Microsoft Graph and PowerShell with per-change approval.
- Enforced strong MFA for all users through a custom authentication strength (Authenticator/TOTP, FIDO2, Windows Hello), disabled SMS and voice, and re-sequenced the cutover so the tenant was never without MFA when Security Defaults was turned off.
- Designed least-privilege admin access: 3 role-assignable groups carrying 7 scoped directory roles, 2 high-risk roles held back for just-in-time PIM, and 2 cloud-only break-glass Global Admins excluded from Conditional Access.
- Onboarded 20 pilot users through one group that drives licensing, MFA policy, MDM enrollment scope, and Intune policy assignment, using 21 of 25 trial seats per SKU.
- Produced audit-ready evidence for every change: 12 snapshots of raw Graph JSON and Microsoft audit logs, each sealed with a SHA-256 manifest and a chain hash, plus a decision log and live-apply journal.
- Kept a 15-entry failed-hypotheses log. Ruled out 4 candidate causes of an opaque Autopilot API error (including missing licensing) and caught 3 wrong role-template IDs and a BitLocker key-escrow bug in the original scripts before they took effect.

## LinkedIn project summary (2 lines)

Built an Intune and Entra ID security baseline for a test tenant from zero: Conditional Access MFA with no SMS or voice, least-privilege role groups, break-glass accounts, BitLocker, and Windows Update rings.
Fully scripted in PowerShell and Microsoft Graph with human approval at every step, SHA-256-sealed evidence, and a public log of every hypothesis I got wrong.

## STAR stories

### 1. Turning off Security Defaults without an MFA gap
- **Situation:** The tenant's only MFA was Security Defaults, and replacing it with Conditional Access is a one-way step.
- **Task:** Move to custom CA-based MFA without a moment where users had no MFA.
- **Action:** In review I found the original script disabled Security Defaults *before* creating any CA policy, and its baseline had no require-MFA rule. I rebuilt the order: SMS and voice off, custom auth strength, require-MFA CA with break-glass excluded, then Security Defaults off. When Graph refused to enable CA while Security Defaults was on, I created the policy in report-only mode, flipped Security Defaults, and enabled the policy in the same session, retrying past a short replication 404.
- **Result:** Custom-strength MFA enforced for all users, Security Defaults off, and no unprotected window. I wrote the corrected order into an SOP.

### 2. Disproving my own root cause (Autopilot)
- **Situation:** Autopilot profile creation failed with an opaque backend 400. I had blamed the missing Entra ID P1 license and published that in an SOP.
- **Task:** Find the real cause without making random changes to the tenant.
- **Action:** I treated P1 as a hypothesis and tested it: activated P1, assigned it, retried. Same error. Then I tested the next candidate, the MDM user scope, with one change and one retry. Same error. I logged each result with its evidence and corrected the SOP.
- **Result:** 4 candidate causes ruled out with captured evidence, a clear next test (portal-created profile comparison, then a Microsoft support case), and a published correction instead of a wrong answer. Still open; I say so plainly.

### 3. A licensing race caused by an undocumented change
- **Situation:** Licensing 20 new pilot users, 7 of 19 direct license calls failed with HTTP 409 concurrency errors.
- **Task:** Work out whether users were left unlicensed and why the calls failed.
- **Action:** I checked each user's license state and the audit logs. The managed-users group already had group-based licensing from an earlier portal change that was never logged, so my direct calls were racing the licensing service.
- **Result:** Confirmed all 20 pilots were licensed through the group (21 of 25 seats). I recommended group-only licensing and added two rules: check a group's licenses before assigning directly, and log every portal-side change.
