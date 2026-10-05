# IT Asset Disposition

- **ID:** `SOP-072`
- **Title:** Secure IT asset disposition (ITAD)
- **Owner:** IT Administrator
- **Status:** draft
- **Created:** 2026-10-05
- **Review date:** 2027-10-05
- **Applies to:** All company-owned devices leaving service
- **Compliance refs:** GLBA Safeguards (secure disposal of customer information); PCI DSS 4.0 Req 3 (protect stored data)

## Purpose

When a device leaves service, the data on it must be unrecoverable and the decision (reuse, donate, resell, destroy) must be documented. Reuse first, destroy last — but destroy properly when it's time.

## TL;DR

Decide: redeploy, donate, resell, or destroy. Sanitize per NIST 800-88 (crypto-erase or overwrite for reuse; physical destruction for dead drives). Get a certificate of destruction for anything destroyed. Log every device's final disposition. Never let a drive leave without sanitization.

## Scope

Covers laptops, desktops, mobile devices, drives, and network equipment. Does not cover paper records (facilities).

## Prerequisites

- Asset removed from MDM and management consoles.
- Data backup/archival completed if the device held anything worth keeping.

## Procedure

### 1. Decide disposition

| Option | When | Sanitization required |
|---|---|---|
| **Redeploy** | Hardware has useful life, meets current baseline | NIST 800-88 Clear or Purge, then reimage |
| **Donate** | Functional but below company spec | Purge; remove asset tags; document recipient |
| **Resell** | Has residual value, data fully sanitized | Purge; document buyer and value |
| **Destroy** | Dead, insecure, or sanitization not verifiable | Physical destruction; certificate required |

Preference order: redeploy → donate → resell → destroy. Cost and sustainability both favor reuse.

### 2. Sanitize

- **Crypto-erase:** For self-encrypting drives, destroy the keys. Fastest, verifiable.
- **Overwrite:** Single-pass overwrite minimum for HDDs bound for reuse. Verify a sample.
- **Physical destruction:** Crush, shred, or disassemble. Required for failed drives and anything that held highly sensitive data where sanitization can't be verified.

### 3. Document

Log for every device: asset tag, serial, disposition, sanitization method, date, who performed it. For destruction: attach the certificate. For donation/resale: record the recipient.

**Expected result:** Every retired device has a disposition record. No drive leaves the building without documented sanitization.

## Verification

- Spot-verify sanitized drives (attempt recovery on a sample).
- Destruction certificates filed and matched to asset tags.
- MDM shows the device as retired/wiped.

## Rollback

Not applicable. Sanitization is one-way by design.

## Exceptions

- **Legal hold:** If a device is subject to litigation hold, do not sanitize or dispose. Isolate, label, and notify legal. The hold overrides this entire procedure.

## Tips & pointers

- Older laptops that can't run the current Windows baseline often make fine Linux machines for donation or lab use. Extending hardware life is both cheaper and more sustainable than shredding working equipment.
- Photograph the asset tags before destruction. Certificates reference serials; having your own record prevents disputes.
- Donation feels good but creates a data-risk tail. Purge thoroughly and get a signed receipt. If you can't verify the sanitization, don't donate it — destroy it.
- Track disposition costs. When leadership sees that reuse saved $X versus buying new, the program funds itself.
