# Customer Data Inventory

- **ID:** `SOP-073`
- **Title:** Customer information inventory and data flow mapping
- **Owner:** IT Administrator
- **Status:** draft
- **Created:** 2026-10-05
- **Review date:** 2027-10-05
- **Applies to:** All systems handling customer information
- **Compliance refs:** GLBA Safeguards (data inventory, access controls)

## Purpose

You can't protect what you haven't mapped. This procedure builds and maintains the inventory of what customer information the organization holds, where it lives, and who can touch it.

## TL;DR

List every system that touches customer data, what data it holds, and who has access. Draw the flows between systems. Review quarterly and whenever a system is added or removed. If you find customer data somewhere it shouldn't be, that's a finding, not a footnote.

## Scope

Covers customer information as defined by GLBA (nonpublic personal information) and cardholder data in PCI scope. Does not cover employee HR data (separate inventory).

## Prerequisites

- List of business processes that handle customer information (sales, finance, service).
- Access to system inventories and the access matrix.

## Procedure

1. **Enumerate systems.** For each business function, list the systems that create, receive, store, or transmit customer information:
   - Sales: CRM, DealerTrack/SSO, document storage, email.
   - Finance: accounting system, lender portals, file shares.
   - Service: payment terminal (cellular, out of network scope), work orders, parts systems.
2. **Classify the data** in each system: names, contact info, financial data, cardholder data, credentials. Note what you do *not* store (e.g., full SSNs, CVVs) — that's a control too.
3. **Map the flows.** For each data type, trace where it enters, where it's stored, where it goes, and where it leaves (including disposal). Diagram it; a paragraph isn't a map.
4. **Map the access.** Who (by role, not name) can read or modify each store? Cross-reference `onboarding/access-matrix.md`.
5. **Identify the surprises.** Data in personal email, local spreadsheets, USB drives, screenshots in chat — these are the findings. Each gets a remediation plan: move it, protect it, or delete it.
6. **Review quarterly** and on every system addition/removal. The inventory is a living document.

**Expected result:** A current diagram showing every customer-data store, its classification, its access list, and the flows between stores. No undocumented copies.

## Verification

- Walk a single customer record through the diagram end to end. Every hop should be on the map.
- Compare the access lists against actual group memberships (access review).

## Rollback

Not applicable.

## Exceptions

There are none. Every system with customer data is in the inventory.

## Tips & pointers

- The most valuable part is step 5. The official systems are always mapped; the shadow copies are where breaches come from. Ask users where they *actually* put things, not where policy says they should.
- Payment data deserves special attention. A cellular terminal keeps card data off the network, but work orders, receipts, and email threads around payments can still carry cardholder data into scope. Follow the paper trail, not just the network diagram.
- Keep the classification simple: public, internal, confidential, restricted. Four buckets people can actually apply beat twelve they can't.
- Date every version of the diagram. When something goes wrong, "what did the map look like in March" is a question you'll be glad you can answer.
