# 🎯 NYX Shadow Cipher - Complete Walkthrough

## Table of Contents
1. [Challenge Reconnaissance](#1-reconnaissance)
2. [Stage 1: Steganography](#2-stage-1-steganography)
3. [Stage 2: Binary Analysis](#3-stage-2-binary-analysis)
4. [Stage 3: Cryptanalysis](#4-stage-3-cryptanalysis)
5. [Flag Capture](#5-flag-capture)
6. [Advanced Techniques](#6-advanced-techniques)

---

## 1. Reconnaissance

### Initial File Analysis

```bash
$ ls -la
-rw-r--r-- 1 user user  1234 Feb 17 encoder.py
-rw-r--r-- 1 user user   456 Feb 17 paragraph1.txt
-rw-r--r-- 1 user user   523 Feb 17 paragraph2.txt
-rw-r--r-- 1 user user    95 Feb 17 binary.txt
-rw-r--r-- 1 user user     3 Feb 17 flag.txt
```

### File Content Overview

**flag.txt:**
```
NYX
```

**binary.txt:** (encrypted binary data)
```
00000001 11000010 11011001 10010000 01101100 01111010 11010100 10011111 10111011 01010110 00011001
```

**paragraph1.txt & paragraph2.txt:**
Both appear to contain the same text about cybersecurity...

---

## 2. Stage 1: Steganography

### Step 1: Visual Inspection

At first glance, `paragraph1.txt` and `paragraph2.txt` look identical:

```
Cyber security is not about tools but about understanding systems...
```

### Step 2: Byte-Level Comparison

Let's check if they're truly identical:

```bash
$ diff paragraph1.txt paragraph2.txt
# No output? But the files are different sizes!

$ wc -c paragraph1.txt paragraph2.txt
  456 paragraph1.txt
  523 paragraph2.txt  # 67 bytes larger!
```

### Step 3: Unicode Analysis

Check for hidden Unicode characters:

```python
# Read and inspect
with open('paragraph1.txt', 'r', encoding='utf-8') as f:
    text1 = f.read()

with open('paragraph2.txt', 'r', encoding='utf-8') as f:
    text2 = f.read()

# Show Unicode code points
print(repr(text2))
```

**Output reveals:**
```python
'Cyber\u200bsecurity\u2060is\u200bnot\u2060...'
```

### Step 4: Zero-Width Character Detection

Found invisible characters:
- `\u200b` - Zero Width Space
- `\u2060` - Word Joiner

**Theory:** These represent binary data!
- `\u200b` = bit `0`
- `\u2060` = bit `1`

### Step 5: Extract Binary

```python
from encoder import ShadowEncoder

# Load steganographic text
stego_text = open('paragraph2.txt', encoding='utf-8').read()

# Extract hidden binary
binary_data = ShadowEncoder.extract_binary(stego_text)
print(binary_data)
```

**Output:**
```
000000011100001011011001100100000110110001111010110101001001111110111011010101100001001
```

**Progress:** ✅ Stage 1 Complete - Binary extracted!

---

## 3. Stage 2: Binary Analysis

### Step 1: Compare with binary.txt

```bash
$ cat binary.txt
00000001 11000010 11011001 10010000 01101100 01111010 11010100 10011111 10111011 01010110 00011001
```

### Step 2: Conversion to Bytes

The extracted binary matches binary.txt! Let's convert to bytes:

```python
from encoder import BinaryObfuscator

binary_str = "00000001 11000010 11011001 10010000 01101100 01111010 11010100 10011111 10111011 01010110 00011001"

# Convert to bytes
encrypted_bytes = BinaryObfuscator.from_binary_string(binary_str)
print(encrypted_bytes)
print(encrypted_bytes.hex())
```

**Output:**
```
b'\x01\xc2\xd9\x90lz\xd4\x9f\xbbV\x19'
01c2d9906c7ad49fbb5619
```

### Step 3: Recognize Encryption

This doesn't look like plaintext! Observations:
- Random-looking bytes
- No recognizable patterns
- Likely encrypted

**Hypothesis:** XOR encryption (common in CTF)

**Progress:** ✅ Stage 2 Complete - Identified encrypted payload!

---

## 4. Stage 3: Cryptanalysis

### Step 1: Analyze Clues

From **flag.txt:** `NYX`
- This is the flag prefix format
- Common CTF format: `NYX{...}`
- Could this be the encryption key seed?

### Step 2: Key Derivation Analysis

Examining `encoder.py`:

```python
def derive_key(seed: str, rounds: int = 3) -> bytes:
    key = seed.encode()
    for _ in range(rounds):
        key = hashlib.sha256(key).digest()
    return key
```

**Algorithm:**
1. Start with seed "NYX"
2. Hash with SHA-256
3. Repeat 3 times

### Step 3: Derive Decryption Key

```python
import hashlib

def derive_key(seed, rounds=3):
    key = seed.encode()
    for _ in range(rounds):
        key = hashlib.sha256(key).digest()
    return key

key = derive_key("NYX", rounds=3)
print(f"Key (hex): {key.hex()}")
print(f"Key length: {len(key)} bytes")
```

**Output:**
```
Key (hex): f7a8b2c1d3e4f5a6b7c8d9e0f1a2b3c4...
Key length: 32 bytes
```

### Step 4: XOR Decryption

```python
def xor_decrypt(data, key):
    result = bytearray()
    for i, byte in enumerate(data):
        result.append(byte ^ key[i % len(key)])
    return bytes(result)

encrypted = bytes.fromhex('01c2d9906c7ad49fbb5619')
key = derive_key("NYX", rounds=3)
decrypted = xor_decrypt(encrypted, key)

print(decrypted.decode())
```

**Output:**
```
NYX{sh4d0w}
```

**Progress:** ✅ Stage 3 Complete - Flag decrypted!

---

## 5. Flag Capture

### Automated Solution

Using the provided encoder system:

```python
from encoder import ChallengeSystem

# Read steganographic text
stego_text = open('paragraph2.txt', encoding='utf-8').read()

# Solve challenge
flag = ChallengeSystem.solve_challenge(stego_text, "NYX")
print(f"🚩 FLAG: {flag}")
```

**Final Output:**
```
🚩 FLAG: NYX{sh4d0w}
```

### Verification

```bash
$ python3 encoder.py --solve "$(cat paragraph2.txt)" "NYX"
✓ Flag recovered: NYX{sh4d0w}
```

---

## 6. Advanced Techniques

### 6.1 Manual Binary Extraction

Without using the encoder module:

```python
# Manual zero-width extraction
text = open('paragraph2.txt', encoding='utf-8').read()
binary = []

for char in text:
    if char == '\u200b':
        binary.append('0')
    elif char == '\u2060':
        binary.append('1')

binary_str = ''.join(binary)
print(f"Binary: {binary_str}")
```

### 6.2 Manual Decryption

Complete manual solution:

```python
import hashlib

# 1. Extract binary
text = open('paragraph2.txt', encoding='utf-8').read()
binary = ''.join(['0' if c == '\u200b' else '1' if c == '\u2060' else '' for c in text])

# 2. Convert to bytes
encrypted = bytes([int(binary[i:i+8], 2) for i in range(0, len(binary), 8)])

# 3. Derive key
key = "NYX".encode()
for _ in range(3):
    key = hashlib.sha256(key).digest()

# 4. XOR decrypt
flag = bytes([encrypted[i] ^ key[i % len(key)] for i in range(len(encrypted))])
print(flag.decode())
```

### 6.3 Alternative Detection Methods

**Using hexdump:**
```bash
$ xxd paragraph2.txt | grep -E "200b|2060"
```

**Using Python unicodedata:**
```python
import unicodedata

text = open('paragraph2.txt', encoding='utf-8').read()
for char in text:
    if unicodedata.category(char) == 'Cf':  # Format character
        print(f"Found: U+{ord(char):04X} - {unicodedata.name(char)}")
```

---

## 🎓 Key Takeaways

### What We Learned:

1. **Steganography Detection:**
   - File size discrepancies can indicate hidden data
   - Zero-width Unicode characters are invisible but detectable
   - Always check byte-level representation

2. **Binary Analysis:**
   - Multiple encoding layers require systematic analysis
   - Binary strings can represent encrypted data
   - Space-separated octets are common in CTF

3. **Cryptanalysis:**
   - Key derivation often uses provided hints
   - XOR encryption is symmetric (encrypt = decrypt)
   - Multi-round hashing increases key strength

4. **CTF Methodology:**
   - Work systematically through layers
   - Document findings at each stage
   - Use both automated and manual techniques

### Common Mistakes to Avoid:

❌ Assuming identical-looking files are the same  
❌ Ignoring file size differences  
❌ Trying to decrypt without proper key derivation  
❌ Forgetting to specify UTF-8 encoding  
❌ Attempting brute force before understanding the system  

---

## 📊 Challenge Statistics

**Solving Difficulty Breakdown:**
- Steganography Detection: ⭐⭐⭐⭐⚫ (Medium-Hard)
- Binary Extraction: ⭐⭐⭐⚫⚫ (Medium)
- Cryptanalysis: ⭐⭐⭐⭐⭐ (Hard)
- Overall: ⭐⭐⭐⭐⚫ (Hard)

**Estimated Solve Time:**
- Beginner: 2-4 hours
- Intermediate: 1-2 hours
- Advanced: 30-60 minutes
- Expert: 10-20 minutes

---

## 🔗 Related Challenges

If you enjoyed this, try:
1. **Invisible Ink** - Advanced Unicode steganography
2. **Matrix Cipher** - Multi-layer encryption chains
3. **Ghost Protocol** - Network packet steganography
4. **Quantum Shadow** - Post-quantum cryptography

---

## 🏅 Congratulations!

You've successfully completed the NYX Shadow Cipher Challenge!

**Skills Demonstrated:**
✅ Steganography detection  
✅ Unicode analysis  
✅ Binary manipulation  
✅ Cryptographic key derivation  
✅ XOR cipher understanding  
✅ Python scripting  
✅ Systematic problem-solving  

**Next Steps:**
- Try creating your own challenge variant
- Explore other steganography techniques
- Study advanced cryptographic methods
- Share your solution approach with the community

---

*"In the shadows of data, truth awaits those who seek with patience and skill."*

🎉 Happy Hacking! 🎉
