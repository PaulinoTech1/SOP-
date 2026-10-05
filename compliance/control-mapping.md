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
| Req 2 — Secure configurations | Harden systems, remove defaults | `workflows/device-hardening.md` (to be written) | Device compliance reports |
| Req 5 — Malware protection | Anti-malware on systems in scope | Endpoint protection policy | Console reports |
| Req 7 — Least privilege | Access limited to job need | `onboarding/new-hire-checklist.md`, `ownership/raci.md` | Access review records |
| Req 8 — Authentication | Unique IDs, MFA, prompt revocation | `onboarding/new-hire-checklist.md`, `onboarding/offboarding-checklist.md` | Identity provider logs |
| Req 9 — Physical access | Restrict physical access to card data | Payment terminal on cellular (out of network scope); facility controls | Network diagrams, terminal config |
| Req 11 — Test security regularly | Quarterly vulnerability scans | `workflows/vulnerability-scanning.md` (to be written) | ASV scan reports |
| Req 12 — Security policies | Documented policies, reviewed annually | This repo | Review dates on each SOP |

**Scoping note:** The payment terminal operates on a cellular connection, keeping cardholder data off the corporate network. This constrains PCI scope. The tradeoff (reduced local visibility, reliance on processor reporting) is documented and accepted.

## GLBA Safeguards Rule

| Safeguard | What it asks | Satisfied by | Evidence |
|---|---|---|---|
| Access controls | Limit access to customer information | `onboarding/new-hire-checklist.md`, role-based groups | Access review records |
| Data inventory | Know what customer info you hold and where | (to be written) | Data flow diagram |
| Encryption | Encrypt customer info at rest and in transit | Device encryption via MDM; TLS for transit | Compliance reports |
| Authentication | MFA for access to customer information systems | `onboarding/new-hire-checklist.md` | Identity provider config |
| Disposal | Secure disposal of customer information | `workflows/asset-disposition.md` (to be written) | Destruction certificates |
| Change management | Test and approve changes affecting safeguards | (to be written) | Change log |
| Incident response | Written response plan | `incident-response/` | Post-incident reviews |

## Gap register

Requirements without a mapped procedure yet. Each needs an SOP or a documented acceptance.

| Requirement | Gap | Plan |
|---|---|---|
| PCI Req 2 | Device hardening procedure not written | Draft `workflows/device-hardening.md` |
| PCI Req 11 | Vulnerability scanning procedure not written | Draft `workflows/vulnerability-scanning.md` |
| GLBA | Data inventory / flow diagram missing | Build from access matrix |
| GLBA | Change management procedure not written | Draft after ticketing is in place |
| GLBA | Asset disposition procedure not written | Draft `workflows/asset-disposition.md` |
