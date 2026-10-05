# Build Log — Thought Process

How and why this repo was built the way it was. Decisions are recorded here so future contributors understand the reasoning, not just the result.

## ADR-001: A repo, not a wiki

**Decision:** SOPs live in a Git repository as Markdown, not in a wiki or a shared drive.

**Why:** Wikis don't have real review workflows, don't lint, and don't version cleanly. A repo gives us pull requests (review before publish), CI (automated checks), blame (who changed what and when), and branches (draft without affecting the live procedures). The SOP lifecycle in the README maps directly onto Git mechanics.

**Tradeoff:** Higher barrier to contribution than a wiki. Mitigated by the template and the start-here path — the goal is that writing a SOP feels like filling in a form, not learning Git.

## ADR-002: Owner and review date are mandatory

**Decision:** Every SOP must name one owner and carry a review date max 12 months out. The linter enforces this.

**Why:** The two most common ways procedures die are "nobody owns it" and "nobody re-read it." Shared ownership is no ownership — exactly one Accountable per RACI. The review date forces a re-validation cycle; a procedure past its date is expired, not active, which prevents people from following stale instructions with false confidence.

## ADR-003: TL;DR and tips (compliance vs. actionability)

**Decision:** Every procedural SOP has three layers: TL;DR at the top, full procedure in the middle, tips & pointers at the bottom.

**Why:** SOPs serve two audiences with opposite needs. Auditors and compliance need the full procedure — complete, precise, traceable. Operators need to know what to do right now, especially under pressure. Documents that lean too far toward compliance don't get read; documents that lean too far toward brevity don't survive audits. The three-layer structure lets each audience read the part they need without compromising the other.

The tips section is deliberately opinionated. It's where the judgment lives — the stuff you learn after doing it ten times that doesn't belong in a formal step but determines whether the procedure actually works.

## ADR-004: The toil register (SOPs as raw material)

**Decision:** Maintain a scored inventory of repetitive tasks alongside the procedures, with an explicit automation pipeline.

**Why:** Documenting a manual process is only half the value. The other half is seeing which processes cost the most and eliminating them. The maturity model (ad-hoc → documented → measured → automated → eliminated) reframes SOPs as the input to automation, not the end state. Without the register, procedures accumulate; with it, they get consumed by automation over time.

The scoring (frequency × time × error risk) prioritizes by cost, and the `eliminated` classification forces the question most teams skip: should this task exist at all?

## ADR-005: Retirement is append-only

**Decision:** Retired SOPs are marked, explained, and preserved. Never deleted. Every retirement gets a log entry with reason, replacement, and approver.

**Why:** Control mappings, audit trails, and incident reviews reference SOPs by ID. Deleting a document breaks the evidence chain for past audits — you can't prove what procedure was in effect in March if the file is gone. The retirement log is itself an audit asset: it proves the organization deliberately manages its procedures.

The four retirement reasons (superseded, eliminated, merged, obsolete) force precision about *why* something is going, which is more useful than a deletion.

## ADR-006: A linter for documents (CI for SOPs)

**Decision:** `scripts/sop-lint.py` validates every SOP on every push, in strict mode.

**Why:** The template and the lifecycle are only as good as their enforcement. Manual review catches content quality; automated checks catch structural decay — blank owners, past-due reviews, dangling references, missing sections. It ran against this repo during construction and immediately found real issues (a malformed date, a missing TL;DR, the template being linted as a live document).

The linter is stdlib-only Python with no dependencies, so it runs anywhere CI runs without supply-chain risk.

## ADR-007: Usage tracking via `last exercised`

**Decision:** Each SOP carries an optional `last exercised` date, updated when the procedure is followed for real. Stale (180+ days) SOPs get flagged.

**Why:** The linter measures structural health; it can't measure whether anyone actually uses the document. A procedure that's structurally perfect but never followed is either unnecessary (retire it), undiscoverable (fix that), or being ignored (a training problem). The three-way triage in SOP-060 turns "stale" from a vague worry into an actionable decision.

## ADR-008: MkDocs for the reading experience

**Decision:** Publish the repo as a searchable documentation site via MkDocs Material.

**Why:** Raw Markdown on GitHub is fine for contributors but poor for the actual audience — new hires, auditors, managers. A documentation site with navigation, search, and readable typography is the difference between a repo people maintain and a tool people use. The `nav` structure in `mkdocs.yml` mirrors the reading path: start here, then role-based sections.

**Tradeoff:** Adds a build step. Kept minimal — `mkdocs build` produces a static site deployable to GitHub Pages with one workflow file.

## Open questions

- **Dangling file references:** The linter checks SOP-XXX cross-references but not Markdown file links. The missing access matrix slipped through for two iterations because of this. Extending the linter is tracked as future work.
- **Health dashboard:** The linter outputs text. A generated Markdown report or badge would make health visible at a glance. Not yet built.
- **Exercise-date discipline:** The `last exercised` system is untested — every field is currently empty. It needs real usage to prove the concept.
