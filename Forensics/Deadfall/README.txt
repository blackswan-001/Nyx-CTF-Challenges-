====================================================
  Deadfall
  Category : Forensics   |   Difficulty : Hard
====================================================

  "The logs will tell you everything.
   If you know how to ask, and which
   clock to believe."
              — IR-ANALYST-01, NRC-2026-0219

====================================================

The drive was found. The image was taken.
The suspect was gone.

But the drive is only part of the picture.
The night of the breach, four systems were
watching. Each one logged what it saw.
None of them agree on when.

Nyx Research's incident response team has
exported logs from every system active
on Sub-level 2 during the breach window.
Your unit has received the full set.

The investigation is yours now.

----------------------------------------------------
  YOUR MISSION
----------------------------------------------------

Reconstruct the timeline.

Six files. Four log sources. One night.
The events are all in there — but they are
spread across systems that speak different
languages, keep different clocks, and one
of which is not telling the full truth.

The picture only becomes clear when you
lay everything against the same clock.

Somewhere in what you find is a confirmation
that the breach happened exactly as the
IR team suspected — and that someone
went to considerable effort to prevent
that confirmation from ever surfacing.

That confirmation is your flag.

But the logs will not hand it to you.
You will have to earn it.

----------------------------------------------------
  THE FILES
----------------------------------------------------

  nightwatch_events.log     NIGHTWATCH event log
  firewall_traffic.log      Perimeter firewall export
  badge_access.log          Physical access control
  auth_events.log           Host authentication log
  network_summary.csv       Aggregated NetFlow data
  duty_officer_report.txt   Duty officer statement

  Each system has its own timezone.
  Each system has its own perspective.
  Not all of them are complete.

----------------------------------------------------
  HINTS  (read only as many as you need)
----------------------------------------------------

Hint 1 — "Three clocks. One truth.
          You cannot read the logs until
          you decide what time it actually is."

Hint 2 — "The gap is not in the data.
          The gap is in the log that
          was supposed to catch everything."

----------------------------------------------------
  TOOLS YOU MAY FIND USEFUL
----------------------------------------------------

  grep, awk, python3, cut, sort
  A timezone converter
  A spreadsheet or timeline tool
  Patience

----------------------------------------------------
  FLAG FORMAT
----------------------------------------------------

  NYX{...}

====================================================
  Nyx Research — Incident Response Division
  Case File : NRC-2026-0219
  Status    : ACTIVE INVESTIGATION
  Clearance : CTF PARTICIPANT ACCESS GRANTED
====================================================