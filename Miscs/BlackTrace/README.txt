====================================================
  Operation AURORA
  Category : OSINT / Phishing   |   Difficulty : Hard
====================================================

  "We pulled four artifacts off the wire before
   the trail went cold. The attacker is still out
   there. Attribution is on you."
                    — NIGHTWATCH Incident Log, Entry 112

====================================================

A credential-harvesting campaign has been running
against financial institutions for three weeks.

847 victims. One attacker. Zero arrests.

The SOC team intercepted email headers, recovered
a phishing kit from a compromised host, captured
C2 panel session logs, and found a developer profile
that keeps coming up in the cross-references.

None of it means anything in isolation.
Together, it points to one person.

Your job is to figure out who.

----------------------------------------------------
  YOUR MISSION
----------------------------------------------------

You have been handed four artifacts pulled from
the investigation.

Somewhere across them is everything you need to
attribute the threat actor — their alias, their
real identity, where they operated from, and the
campaign they were running.

Read carefully. Cross-reference everything.
The flag is the attribution.

----------------------------------------------------
  THE ARTIFACTS
----------------------------------------------------

  Four pieces. One picture.

  Not every field is relevant.
  Not every value is what it appears to be.

  [ index.html ]

----------------------------------------------------
  HINTS  (read only as many as you need)
----------------------------------------------------

Hint 1 — "The flag is an attribution, not a
          password. It has four parts: who they
          called themselves, who they actually
          are, where they were, and what they
          named the operation. The artifacts
          between them answer all four."

Hint 2 — "Identity is never just one source.
          A name in a config file and a face
          on a profile are two halves of the
          same answer."

Hint 3 — "The operator logged in. Logs record
          where from. Geolocation does the rest."

----------------------------------------------------
  FLAG FORMAT
----------------------------------------------------

  NYX{...}

====================================================
  Nyx Research — Incident Response Division
  Case File : CYB-2024-PH-0047
  Status    : ACTIVE INVESTIGATION
  Clearance : CTF PARTICIPANT ACCESS GRANTED
====================================================