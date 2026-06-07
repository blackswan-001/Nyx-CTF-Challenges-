========================================
     Nyx Protocol
     Category : Reverse Engineering
     Difficulty : Hard
========================================

------------------------------
Description:
------------------------------
The gate does not yield to guessing.
The gate does not yield to patience.

It yields only to those who understand
what happens between input and verdict.

An 8-character access key is required.
Find it.

-------------------------------------
Hint (optional, release if needed):
-------------------------------------
"The key is not stored.
 It is recognized."

-------------
Flag Format:
-------------
NYX{...}

------------------------------------------------------------
File
------------------------------------------------------------

nyx_protocol   (ELF 64-bit, stripped)

Run on Linux:
    chmod +x nyx_protocol
    ./nyx_protocol

The program runs until the correct key is entered
or the session is terminated (Ctrl+C).

========================================