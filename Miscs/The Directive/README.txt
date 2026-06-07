====================================================
  The Directive
  Category : Miscellaneous   |   Difficulty : Upper-Medium
====================================================

  "Hale was a door. Someone else built the frame."
                              — NIGHTWATCH final log entry

====================================================

The investigation into the Nyx Research breach is
not closed.

Nathan Hale has been identified. His access patterns
confirmed. His deleted files recovered. His badge
exit logged at 23:58 UTC with no return record.

But the incident response team has hit a wall.

Hale was an actor. The evidence is clear on that.
What the evidence does not show — what no case file
has yet established — is who gave the order.

The NIGHTWATCH automated signal network logged one
final transmission before it was taken offline from
inside. The system was shut down by someone who knew
exactly where the kill switch was.

That transmission was never decoded.

Until now.

This briefing package was distributed exclusively
to senior IR analysts. It was never meant to leave
the division.

You have it now.

----------------------------------------------------
  YOUR MISSION
----------------------------------------------------

Two artefacts remain from NIGHTWATCH's final log.

One is a sealed sensor capture — an image from the
last active monitoring node before the system went
dark. It looks like noise. It is not noise.

One is an intercepted transmission — a message that
went out just before the shutdown. It is encoded.
The encoding was deliberate. Someone wanted it to
survive, but not to be read easily.

Both artefacts are required.
Neither is sufficient alone.

Decode the transmission.
Confirm the source.
The flag is your authorisation token.

----------------------------------------------------
  WHAT YOU KNOW
----------------------------------------------------

  Case NRC-2026-0112 — Midnight Habits
  Breach vector confirmed. Credential reconstruction
  via open-source profiling. Hale was the entry point.

  Case NRC-2026-0219 — NIGHTWATCH Archive
  Hale's comms intercepted. Deleted files recovered.
  Badge exit confirmed. No return record.

  Case NRC-2026-CLASSIFIED — The Directive
  Origin of the directive: unknown.
  NIGHTWATCH final transmission: unread.
  This is where the trail leads.

----------------------------------------------------
  THE ARTEFACTS
----------------------------------------------------

  [ signal_capture   ]  NIGHTWATCH sensor image
                        Node 07 — final log entry
                        Status : SEALED

  [ transmission     ]  Intercepted outgoing message
                        Encoding : UNKNOWN
                        Source   : NIGHTWATCH relay node

----------------------------------------------------
  HINTS  (read only as many as you need)
----------------------------------------------------

Hint 1 — "The image is sealed. But sealed things
          can be opened — if you know the name
          of the operation."

Hint 2 — "What you extract from the image is not
          the answer. It is the key to the answer."

Hint 3 — "The QR code and the page tell you the
          same thing. You need what the hash
          gives you before either is useful."

----------------------------------------------------
  TOOLS YOU MAY FIND USEFUL
----------------------------------------------------

  steghide
  hash-identifier
  hashcat + rockyou.txt
  A QR code reader
  A Vigenere decoder (CyberChef, dcode.fr)

----------------------------------------------------
  FLAG FORMAT
----------------------------------------------------

  NYX{...}

====================================================
  Nyx Research — Incident Response Division
  Case File : NRC-2026-CLASSIFIED
  Status    : ACTIVE — ESCALATED
  Clearance : SENIOR IR ANALYSTS ONLY
====================================================