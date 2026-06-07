# 🏛️ Nyx CTF — Post-Event Infrastructure & Challenge Showcase

This repository serves as the official production archive and post-event engineering showcase for the **Nyx CTF** competition, designed, deployed, and managed for our annual department symposium. 

Rather than a static collection of files, this codebase represents a battle-tested infrastructure matrix that successfully sustained active, adversarial traffic from **40 concurrent teams (160+ live players)** over a high-intensity multi-hour competition window.

---

## 📊 Live Infrastructure & Incident Response (IR) Metrics

Managing an environment under real-time player traffic provided a massive, live-fire lesson in platform reliability engineering, threat policy enforcement, and disaster recovery:

*   **The Incident (Resource Exhaustion DoS)**: During the live event, players initiated unauthorized, aggressive directory brute-forcing using automated tools like `gobuster` and `dirbuster`. This unexpected multi-threaded traffic surge flooded our reverse proxy, exhausted system resources, and triggered a complete platform outage.
*   **The Tactical Pivot (Traffic Rerouting)**: To immediately bypass routing complications at the edge, our team initiated an emergency incident response protocol—dropping the active Cloudflare proxy layer and establishing direct IP routing straight to our bare-metal host machine.
*   **The Remediation (Container Overhaul)**: We hot-swapped our configurations on the fly: manually overhauling the backend `nginx.conf` reverse-proxy architectures, clearing the corrupted application states, and executing a clean Docker environment rebuild.
*   **The Resolution (Phased Throttled Rollout)**: To eliminate the risk of a secondary traffic spike upon system boot, we enforced an immediate ban on automated brute-force tools. We temporarily reduced our attack surface by pulling back the vulnerable web exploit challenges, and successfully executed a **throttled, batch-by-batch deployment of our 26 challenges over a 3-hour window**, restoring 100% platform availability without dropping the core scoring database.

---

## 📁 Repository Blueprint & Engineering Vectors

Each category folder is fully self-contained, containing raw source configurations, player-facing deployment assets, and our intended automation solve paths:

*   `./Forensics/`: Network packet analysis and system log parsing tasks. Includes `dead_frequencies.pcap`—a synthetic network traffic dump constructed programmatically from scratch using custom Python scripts and **Scapy** to inject obfuscated data layers (e.g., DNS tunneling simulations).
*   `./Web Exploits/`: Hardened challenges simulating modern application flaws, including session token vulnerabilities, authorization bypasses, and injection points (`RootMe`, `Secure Vault`).
*   `./Reverse Engineering/`: Compiled binaries and source architectures (`hidden.c`, `NYXProtocol.c`) designed to test low-level logic decoding and static/dynamic binary analysis.
*   `./Miscs/`: Multilayer data manipulation, custom encoding algorithms, cryptographic scripts, and programmatic automation solvers (`Multilayer Madness`, `Shadow Cipher`).
*   `./OSINT/`: Open-source intelligence tracks built inside localized, sandboxed environments (`Ghost Tracer`, `Midnight Habits`) utilizing archived historical structures and custom Docker packages.
*   `./Warmups/`: Foundational cryptographic and logic entry points designed to establish operational baselines for competing teams.

---

## 🎯 Architecture Philosophy

1.  **Code-Driven Design**: Challenges requiring data generation (like network traffic dumps or custom ciphers) were built via reproducible, automated Python scripts rather than manual captures.
2.  **Isolated Deliverables**: Every challenge folder isolates the player payload from the developer's internal solve paths and automated verify scripts, serving as an open-source security laboratory reference.
3.  **Resilience Focused**: Designed to demonstrate how security tools function under real-world infrastructure constraints, constraints tracking, and active multi-session execution environments.
