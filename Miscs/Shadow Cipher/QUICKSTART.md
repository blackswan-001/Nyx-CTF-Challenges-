# 🚀 NYX Shadow Cipher - Quick Start Guide

## What is this?

A **challenging CTF puzzle** that combines:
- 🔍 **Zero-Width Steganography** - Hidden data in plain text
- 🔐 **XOR Cryptography** - Multi-layer encryption
- 🧩 **Binary Obfuscation** - Encoded payloads

**Difficulty:** Hard (8/10) | **Estimated Time:** 1-3 hours

---

## 📦 What You Get

```
📁 NYX-Shadow-Cipher/
├── 🐍 encoder.py           # Main challenge system
├── 📄 paragraph1.txt       # Reference text
├── 📄 paragraph2.txt       # Suspicious text (identical?)
├── 📄 binary.txt           # Encrypted payload
├── 📄 flag.txt             # Hint
├── 📖 README.md            # Full documentation
├── 📖 WALKTHROUGH.md       # Step-by-step solution
└── 🧪 test_challenge.py    # Verification suite
```

---

## ⚡ Instant Start

### Option 1: Interactive Mode (Recommended for Beginners)
```bash
python3 encoder.py
```
This launches an interactive challenge interface with:
- Progressive hint system
- Flag validation
- Solution guidance

### Option 2: Direct Solve (For Advanced Users)
```bash
# Extract hidden binary
python3 encoder.py --extract "$(cat paragraph2.txt)"

# Solve completely
python3 encoder.py --solve "$(cat paragraph2.txt)" "NYX"
```

### Option 3: Test Everything Works
```bash
python3 test_challenge.py
```

---

## 🎯 Your Mission

Find the hidden flag in format: **NYX{...}**

**Clues:**
1. Two paragraphs look the same... but are they?
2. Invisible characters tell stories
3. The flag format is the key
4. Three stages must be conquered

---

## 💡 Need Help?

### Level 1 Hints (Spoiler-Free)
- Compare file sizes
- Look for Unicode anomalies
- Check what "NYX" means

### Level 2 Hints (Mild Spoilers)
- Zero-width characters: U+200B, U+2060
- Binary representation hidden in text
- XOR encryption with derived key

### Level 3 - Full Solution
- See **WALKTHROUGH.md** for complete step-by-step

---

## 🔧 Requirements

```bash
# Python 3.7+
python3 --version

# No external dependencies needed!
# Everything uses Python standard library
```

---

## 🎓 What You'll Learn

By solving this challenge:
- ✅ Zero-width steganography detection
- ✅ Unicode character manipulation
- ✅ Binary to bytes conversion
- ✅ XOR cipher mechanics
- ✅ SHA-256 key derivation
- ✅ Multi-stage CTF problem solving

---

## 📚 Documentation

| File | Purpose |
|------|---------|
| **README.md** | Full challenge documentation |
| **WALKTHROUGH.md** | Complete solution with explanations |
| **This file** | Quick start guide |

---

## 🏆 Challenge Modes

### 🟢 Easy Mode
```bash
python3 encoder.py  # Use the interactive interface
```

### 🟡 Medium Mode
```bash
# Use encoder.py helper functions but write your own solution
```

### 🔴 Hard Mode
```bash
# Solve manually without using encoder.py
# Only use: paragraph1.txt, paragraph2.txt, binary.txt, flag.txt
```

### ⚫ Nightmare Mode
```bash
# Modify encoder.py to add another encryption layer
# Make your own harder version!
```

---

## ⚙️ Command Reference

```bash
# Interactive mode
python3 encoder.py

# Show help
python3 encoder.py --help

# Extract binary from text
python3 encoder.py --extract "your text with hidden data"

# Solve challenge
python3 encoder.py --solve "stego_text" "key_prefix"

# Create new challenge
python3 encoder.py --create "NYX{your_flag}" "cover text"

# Run tests
python3 test_challenge.py
```

---

## 🎮 Try These Commands

```bash
# 1. Compare the paragraphs
diff paragraph1.txt paragraph2.txt
wc -c paragraph1.txt paragraph2.txt

# 2. Look for hidden Unicode
python3 -c "print(repr(open('paragraph2.txt').read()[:100]))"

# 3. Check binary format
cat binary.txt

# 4. Read the hint
cat flag.txt

# 5. Start the challenge
python3 encoder.py
```

---

## ❓ FAQ

**Q: Where do I start?**  
A: Run `python3 encoder.py` for interactive mode!

**Q: I'm stuck, what now?**  
A: Check README.md hints section, or use `--help` flag

**Q: Can I see the solution?**  
A: Yes! WALKTHROUGH.md has complete explanations

**Q: Is this beginner-friendly?**  
A: Challenging but educational. Start with interactive mode!

**Q: Can I modify this challenge?**  
A: Absolutely! Use `--create` to make your own versions

---

## 🌟 Features

- ✨ **Multi-layered** - 3 distinct challenge stages
- 🎯 **Educational** - Learn real steganography techniques
- 🔧 **Extensible** - Create your own variants
- 📚 **Well-documented** - Full walkthrough included
- ✅ **Tested** - Automated test suite included
- 🎨 **Interactive** - Hint system for guidance

---

## 🚀 Ready to Start?

Pick your path:

```bash
# Beginner → Interactive guided mode
python3 encoder.py

# Intermediate → Use tools, solve yourself
python3 encoder.py --help

# Advanced → Manual solution
# (Just use the .txt files)

# Expert → Create harder version
python3 encoder.py --create "NYX{new_flag}" "new text"
```

---

## 🎉 Good Luck!

*"In darkness, only those who seek shall find"*

**Remember:** Every expert was once a beginner who didn't give up!

Need help? Check README.md → Hints Section

---

## 📞 Support

- 📖 Full Docs: README.md
- 📝 Solution: WALKTHROUGH.md
- 🧪 Testing: test_challenge.py
- 💻 Tool Help: `python3 encoder.py --help`

**Happy Hacking! 🔓**
