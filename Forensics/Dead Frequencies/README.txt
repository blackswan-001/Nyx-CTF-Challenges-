====================================================
  Dead Frequencies
  Category : Forensics   |   Difficulty : Hard
====================================================

  "The insider went dark three weeks ago.
   This is the last capture we have."
                    — NIGHTWATCH Incident Log, Entry 47

====================================================

Three weeks ago, a Nyx Research employee stopped
showing up.

No notice. No forwarding address. No explanation.

What they left behind was a workstation, a dead
badge, and a gap in the archives that nobody can
fully account for. NIGHTWATCH flagged the anomaly
four hours after the fact — too late to catch the
exfiltration in progress, but early enough to pull
one thing off the wire:

A network capture. Twelve minutes of traffic from
the insider's machine. The last active session
before they went dark.

It has been sitting in the incident queue ever since.
Nobody has been able to tell us what was sent out,
or how.

That changes now.

----------------------------------------------------
  YOUR MISSION
----------------------------------------------------

You have been handed the capture file.

Somewhere inside it is evidence of what was
exfiltrated — data that was pulled out of Nyx
Research systems and sent somewhere it was never
supposed to go.

The traffic is noisy. It was always noisy on that
machine. Whether that noise is natural or
manufactured, we cannot say.

What we can say is this: something real is in there.
Something that was not meant to be found.

Find it.

Reconstruct what was sent.
Confirm the exfiltration path.
The flag is what was taken.

----------------------------------------------------
  THE CAPTURE
----------------------------------------------------

  Twelve minutes. One machine. One session.

  Not everything you see is relevant.
  Not everything relevant is obvious.

  [ dead_frequencies.pcap ]

----------------------------------------------------
  HINTS  (read only as many as you need)
----------------------------------------------------

Hint 1 — "The noise is loud because it was meant
          to be. Look past it. Filter first,
          read second."

Hint 2 — "Some protocols were built to carry data
          in places people forget to check.
          The domain isn't real.
          The data inside it is."

----------------------------------------------------
  TOOLS YOU MAY FIND USEFUL
----------------------------------------------------

  Wireshark
  tshark
  base64

  The exfiltration method is real.
  The tools to find it are standard.

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