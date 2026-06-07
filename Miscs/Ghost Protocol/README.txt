====================================================
  Ghost Protocol
  Category : Flagship   |   Difficulty : Hard
====================================================

  "The contractor doesn't know who hired them.
   That's the point."
                    — RC-OPS-7F dead drop, recovered

====================================================

You already know the firm.

redcellsec. Boutique offensive security. Operator
v0idwalker. CVE-2023-44487. The HTTP/2 campaign that
hammered three CDN providers simultaneously while
something else was happening somewhere else entirely.

The campaign was noise. Coordinated, professional,
deliberately timed noise.

Someone needed four hours of chaos on the internet
while they walked through a door inside Nyx Research.
They hired redcellsec to provide it. They paid well
enough that no questions were asked.

One question was never asked:

Who was the client?

redcellsec kept them compartmentalised. No name in
any brief. No identifier in any log. Just an internal
designator that meant nothing to anyone who didn't
already know.

A dead drop surfaced three days after the operation
closed. A contractor brief that should have been
destroyed. An ops archive that was never meant to
leave node RC-OPS-7F. A signal capture from the last
moment before the node went dark.

Someone sent a transmission just before shutdown.
It was intercepted. It has not been decoded.

Until now.

----------------------------------------------------
  YOUR MISSION
----------------------------------------------------

Three files were recovered from the dead drop.

Work through them. The layers do not announce
themselves. False signals have been placed
deliberately — some will decode to plausible output.
Plausible is not correct.

Identify the client.
The flag is your confirmation.

----------------------------------------------------
  THE DEAD DROP — THREE FILES
----------------------------------------------------

  [ contractor_brief.html ]
    Redcellsec internal operations brief for
    WRAITHLINE. Contains session authentication
    tokens and operation parameters.

  [ signal_drop.txt ]
    Recovered paste from the RC-OPS dead drop
    channel. Post-operation activity log.
    Auth tokens flagged for analysis.

  [ ops_archive.html ]
    Node RC-OPS-7F sealed ops archive. Contains
    the final sensor capture and an intercepted
    outgoing transmission. Neither is what it
    appears to be.

----------------------------------------------------
  HINTS  (read only as many as you need)
----------------------------------------------------

Hint 1 — "Not every encoded string is a fragment.
          Some are noise. The ones that matter
          are in the right places — not the
          obvious ones."

Hint 2 — "The codename tells you more than
          it says. Count carefully."

Hint 3 — "Ghost Ping used NYX[0] as an XOR key.
          Patterns repeat."

----------------------------------------------------
  TOOLS YOU MAY FIND USEFUL
----------------------------------------------------

  CyberChef
  hash-identifier
  hashcat + rockyou.txt
  steghide
  A Rail Fence decoder
  python3

----------------------------------------------------
  FLAG FORMAT
----------------------------------------------------

  NYX{...}

====================================================
  Ghost Protocol — Flagship Challenge
  Unlocks at    : 3500 points
  Prior case    : Ghost Ping (NYX{v0idwalker_redcellsec_CVE-2023-44487})
  Status        : ACTIVE
====================================================