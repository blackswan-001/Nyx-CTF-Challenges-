# NYX Shadow Cipher Challenge 🕵️‍♂️

## 🎯 Challenge Overview

**Difficulty:** ████████░░ (8/10) - Hard  
**Category:** Cryptography + Steganography + OSINT  
**Skills Required:** Binary analysis, Unicode manipulation, XOR cryptography, Python scripting

A multi-layered CTF challenge combining zero-width steganography, custom XOR encryption, and binary obfuscation. Can you uncover the shadow hidden in plain sight?

---

## 📦 Challenge Files

```
├── encoder.py         # Challenge system and solver tools
├── paragraph1.txt     # Clean reference text
├── paragraph2.txt     # Suspicious text (looks identical?)
├── binary.txt         # Encrypted binary payload
├── flag.txt           # Partial clue
└── README.md          # This file
```

---

## 🎮 Quick Start

### Run Interactive Mode
```bash
python3 encoder.py
```

### Get Help
```bash
python3 encoder.py --help
```

---

## 🧩 Challenge Structure

This challenge consists of **THREE MAIN STAGES**:

### Stage 1: Steganography Detection 🔍
- Compare `paragraph1.txt` and `paragraph2.txt`
- They look identical... or do they?
- **Hint:** Not all whitespace is visible to the naked eye

### Stage 2: Binary Extraction 📊
- Decode the hidden data from paragraph2.txt
- Understand the relationship with binary.txt
- **Hint:** Unicode has secrets beyond ASCII

### Stage 3: Cryptographic Decryption 🔐
- Use the clue from flag.txt
- Apply proper key derivation
- Decrypt the final payload
- **Hint:** The flag format is part of the puzzle

---

## 💡 Hints (Reveal Gradually)

<details>
<summary><b>Hint 1 - Detection</b></summary>

Use a hex editor or Python to compare the two paragraph files byte-by-byte. Look for differences in the Unicode representation.

```bash
python3 -c "print(repr(open('paragraph2.txt').read()))"
```
</details>

<details>
<summary><b>Hint 2 - Zero-Width Characters</b></summary>

The file contains zero-width Unicode characters:
- `\u200b` - Zero Width Space (represents binary 0)
- `\u2060` - Word Joiner (represents binary 1)

Extract these to recover a binary string.
</details>

<details>
<summary><b>Hint 3 - Extraction Method</b></summary>

```python
from encoder import ShadowEncoder

stego_text = open('paragraph2.txt', encoding='utf-8').read()
binary_data = ShadowEncoder.extract_binary(stego_text)
print(binary_data)
```
</details>

<details>
<summary><b>Hint 4 - Cryptography</b></summary>

The binary represents XOR-encrypted data. The key is derived from "NYX" using:
- SHA-256 hashing
- 3 rounds of iteration
- Use the flag prefix from flag.txt
</details>

<details>
<summary><b>Hint 5 - Complete Solution</b></summary>

```python
from encoder import ChallengeSystem

stego_text = open('paragraph2.txt', encoding='utf-8').read()
flag = ChallengeSystem.solve_challenge(stego_text, "NYX")
print(f"Flag: {flag}")
```
</details>

---

## 🛠️ Tools & Techniques

### Manual Analysis
1. **Hex Editors:** HxD, xxd, hexdump
2. **Unicode Inspectors:** Unicode code point analysis
3. **Python Libraries:** unicodedata, binascii

### Automated Solving
```bash
# Extract hidden binary
python3 encoder.py --extract "$(cat paragraph2.txt)"

# Full solution
python3 encoder.py --solve "$(cat paragraph2.txt)" "NYX"
```

---

## 🎓 Learning Objectives

By solving this challenge, you will understand:

1. **Zero-Width Steganography**
   - How invisible Unicode characters can hide data
   - Detection techniques for hidden content

2. **XOR Encryption**
   - Key derivation using cryptographic hashing
   - Multi-round encryption schemes

3. **Binary Encoding**
   - Binary to text conversion methods
   - Space-separated octet representation

4. **CTF Methodology**
   - Multi-stage puzzle solving
   - Combining different cryptographic techniques

---

## 🏆 Success Criteria

You've successfully solved the challenge when you:
- ✅ Extracted the hidden binary from paragraph2.txt
- ✅ Understood the encryption mechanism
- ✅ Derived the correct decryption key
- ✅ Recovered the flag in format: `NYX{...}`

---

## 🔧 Advanced: Create Your Own Challenge

```bash
# Create a new challenge with custom flag and text
python3 encoder.py --create "NYX{your_flag}" "Your cover text here with enough words"
```

**Requirements:**
- Flag must start with `NYX{` and end with `}`
- Cover text needs enough spaces for binary data
- Approximately 8 bits per character in flag

---

## 📚 Technical Deep Dive

### Steganography Engine
```python
class ShadowEncoder:
    ZERO = '\u200b'  # Zero Width Space = bit 0
    ONE = '\u2060'   # Word Joiner = bit 1
```

### Key Derivation
```python
def derive_key(seed, rounds=3):
    key = seed.encode()
    for _ in range(rounds):
        key = hashlib.sha256(key).digest()
    return key
```

### Encryption Flow
```
Flag → XOR Encrypt → Binary String → Zero-Width Encoding → Stego Text
```

### Decryption Flow
```
Stego Text → Extract Binary → Bytes → XOR Decrypt → Flag
```

---

## 🐛 Troubleshooting

**Problem:** Can't see difference between paragraphs  
**Solution:** Use `xxd` or Python's `repr()` to view raw bytes

**Problem:** Binary extraction returns empty string  
**Solution:** Ensure proper UTF-8 encoding when reading files

**Problem:** Decryption fails  
**Solution:** Verify you're using correct flag prefix for key derivation

---

## 🎖️ Challenge Variants

Want more difficulty? Try these modifications:

1. **Hard Mode:** Derive key from SHA-512 with 5 rounds
2. **Expert Mode:** Add AES encryption layer before XOR
3. **Nightmare Mode:** Use multiple zero-width characters (4+ types)
4. **Custom Mode:** Create your own obfuscation method

---

## 👥 Credits

**Challenge Type:** Cryptography + Steganography  
**Techniques Used:** Zero-width Unicode, XOR cipher, Binary encoding  
**Inspired By:** Real-world APT steganography techniques  

---

## 📖 Additional Resources

- [Unicode Zero-Width Characters](https://en.wikipedia.org/wiki/Zero-width_space)
- [XOR Cipher Theory](https://en.wikipedia.org/wiki/XOR_cipher)
- [Steganography in Cybersecurity](https://www.sans.org/reading-room/whitepapers/stenganography/)

---

## 🚀 Ready to Start?

```bash
python3 encoder.py
```

**Remember:** *"In darkness, only those who seek shall find"*

Good luck, hacker! 🔓
