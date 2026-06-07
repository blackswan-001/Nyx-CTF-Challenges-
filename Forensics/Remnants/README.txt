====================================================
  Remnants
  Category : Forensics   |   Difficulty : Medium-Hard
====================================================

  "He had seven minutes.
   Apparently, he thought that was enough."
                    — IR Team Lead, Case NRC-2026-0219

====================================================

The drive was handed in wiped.

That was the plan, anyway. Seven minutes at the
terminal — enough time to delete everything, pull
the drive, and walk out. The badge logs confirm
he made it as far as the exit.

What he left behind was a 10MB FAT32 image and
the assumption that deleted means gone.

It doesn't.

The Nyx Research incident response team has imaged
the drive and passed it to your unit. Whatever was
on it — documents, logs, communications — was
deleted before seizure. The filesystem shows nothing.

That's where you come in.

----------------------------------------------------
  YOUR MISSION
----------------------------------------------------

Recover what was deleted.

The files on this drive were part of an active
investigation into the breach of Nyx Research
systems. Someone wanted them gone badly enough
to risk everything on a seven-minute window.

Find out why.

Recover the files. Read them carefully.
The evidence is fragmented. The picture only
becomes clear when you assemble all of it.

Somewhere in what you recover is a confirmation
that ties this drive directly to the breach.
That confirmation is your flag.

But it won't be handed to you plainly.
Someone made sure of that too.

----------------------------------------------------
  THE DRIVE
----------------------------------------------------

  One image. Ten megabytes.
  Eight files. All deleted.
  None of them truly gone.

  [ remnants.img ]

----------------------------------------------------
  HINTS  (read only as many as you need)
----------------------------------------------------

Hint 1 — "Deleted doesn't mean gone.
          The right tool reads what the
          filesystem refuses to show."

Hint 2 — "Everything you need to decode
          what you find is already in
          the files you recover.
          Read all of them."

----------------------------------------------------
  TOOLS YOU MAY FIND USEFUL
----------------------------------------------------

  foremost
  unzip
  A PDF viewer
  A Caesar cipher decoder

  The deletion method is standard.
  The tools to undo it are standard.
  What you do with what you find
  is the challenge.

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