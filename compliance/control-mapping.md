# Control Mapping — PCI DSS & GLBA

- **ID:** `SOP-030`
- **Title:** Compliance control mapping
- **Owner:** IT Administrator
- **Status:** draft
- **Created:** 2026-10-05
- **Review date:** 2027-10-05
- **Applies to:** All systems in scope for PCI DSS and GLBA

## Purpose

Maps each compliance requirement to the procedure that satisfies it. Auditors get this document; it points them at the SOP that proves the control. If a requirement has no mapped procedure, that's a gap, and gaps get tracked, not hidden.

## PCI DSS 4.0 (SAQ scope)

| Requirement | What it asks | Satisfied by | Evidence |
|---|---|---|---|
| Req 2 — Secure configurations | Harden systems, remove defaults | `workflows/device-hardening.md` (SOP-070) | Device compliance reports |
| Req 5 — Malware protection | Anti-malware on systems in scope | Endpoint protection policy | Console reports |
| Req 7 — Least privilege | Access limited to job need | `onboarding/new-hire-checklist.md`, `ownership/raci.md` | Access review records |
| Req 8 — Authentication | Unique IDs, MFA, prompt revocation | `onboarding/new-hire-checklist.md`, `onboarding/offboarding-checklist.md` | Identity provider logs |
| Req 9 — Physical access | Restrict physical access to card data | Payment terminal on cellular (out of network scope); facility controls | Network diagrams, terminal config |
| Req 11 — Test security regularly | Quarterly vulnerability scans | `workflows/vulnerability-scanning.md` (SOP-071) | ASV scan reports |
| Req 12 — Security policies | Documented policies, reviewed annually | This repo | Review dates on each SOP |

**Scoping note:** The payment terminal operates on a cellular connection, keeping cardholder data off the corporate network. This constrains PCI scope. The tradeoff (reduced local visibility, reliance on processor reporting) is documented and accepted.

## GLBA Safeguards Rule

| Safeguard | What it asks | Satisfied by | Evidence |
|---|---|---|---|
| Access controls | Limit access to customer information | `onboarding/new-hire-checklist.md`, role-based groups | Access review records |
| Data inventory | Know what customer info you hold and where | `workflows/data-inventory.md` (SOP-073) | Data flow diagram |
| Encryption | Encrypt customer info at rest and in transit | Device encryption via MDM; TLS for transit | Compliance reports |
| Authentication | MFA for access to customer information systems | `onboarding/new-hire-checklist.md` | Identity provider config |
| Disposal | Secure disposal of customer information | `workflows/asset-disposition.md` (SOP-072) | Destruction certificates |
| Change management | Test and approve changes affecting safeguards | `workflows/change-management.md` (SOP-074) | Change log |
| Incident response | Written response plan | `incident-response/` | Post-incident reviews |

## Gap register

Requirements without a mapped procedure yet. Each needs an SOP or a documented acceptance.

| Requirement | Gap | Status |
|---|---|---|
| PCI Req 2 | Device hardening procedure | Done — `workflows/device-hardening.md` (SOP-070) |
| PCI Req 11 | Vulnerability scanning procedure | Done — `workflows/vulnerability-scanning.md` (SOP-071) |
| GLBA | Data inventory / flow diagram | Done — `workflows/data-inventory.md` (SOP-073) |
| GLBA | Change management procedure | Done — `workflows/change-management.md` (SOP-074) |
| GLBA | Asset disposition procedure | Done — `workflows/asset-disposition.md` (SOP-072) |
