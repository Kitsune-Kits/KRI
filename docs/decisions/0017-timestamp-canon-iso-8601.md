# ADR-0017: Timestamp canon: ISO 8601-1 everywhere a clock is written

- **Status:** Proposed
- **Date:** 2026-11-19
- **Persona:** ⚡ Piko (lead)
- **Scope:** org-wide

## Context

The forge writes deadlines and records across tools that disagree
about dates: diaries, ledgers, CI stamps, chat surfaces, and the
classic trap, a same-evening local deadline stated in one timezone and
read in another. ISO 8601-1:2019 is the international standard for
date and time representations in information interchange, and the
forge already half-obeys it: the Forge Diary's dates are ISO-ordered by
convention. The gap is the unstated half: times, offsets, and
countdown math.

## Decision

1. **Record fields** (diaries, ledgers, ADR dates, bench logs) use
   YYYY-MM-DD exactly; date-time fields use extended format with an
   explicit UTC offset, e.g. 2027-05-27T19:00:00-04:00.
2. **Deadlines** are stated in the target venue's local time with the
   offset written next to them once; countdowns are computed from the
   offset-qualified instant, so an 8 PM ET deadline can never be read
   as 8 PM elsewhere.
3. Machine-generated stamps in forge tooling emit offset-qualified
   ISO 8601-1 strings; human prose may say "Thursday" like a person,
   as long as the record field beside it is canonical.
4. Existing records are not edited to comply; the canon applies forward
   from this ADR's ratification.

## Consequences

- Deadlines and stamps stop depending on the reader's timezone
  assumptions; countdown math becomes deterministic.
- Cost: essentially zero. This ratifies current practice, which is
  the cheapest kind of standard.
- Blast radius: every repo's logs and status files, forward only.
