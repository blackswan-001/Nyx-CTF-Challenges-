====================================================
  Echo Chamber
  Category : Forensics   |   Difficulty : Warmup
====================================================

Before you can find the Protocol,
you must learn to listen.

A server log has been recovered from a machine
that was running under a storm of noise.

SSH daemons. Cron jobs. Docker containers.
Web requests. Auth failures. System chatter.

Somewhere inside that noise — a signal repeats.
Something that does not belong.
Something that, piece by piece, says something.

This is where it begins.
Not every system is silent.
Some of them are already talking.

----------------------------------------------------
  YOUR MISSION
----------------------------------------------------

Analyse log.txt.

Find what repeats.
Find what it carries.
Decode it.

----------------------------------------------------
  HINTS  (read only as many as you need)
----------------------------------------------------

Hint 1 — "Not every login failure is random."

Hint 2 — "One source is more persistent than the others.
          Look at what that source leaves behind."

----------------------------------------------------
  TOOLS YOU MAY FIND USEFUL
----------------------------------------------------

  grep, awk, python3, CyberChef

  A pattern that appears in the suspicious lines
  but not in the clean ones is a good place to start.

----------------------------------------------------
  FLAG FORMAT
----------------------------------------------------

  NYX{...}

====================================================