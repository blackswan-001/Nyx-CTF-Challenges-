#!/usr/bin/env python3
"""
NYX Shadow Cipher - Interactive Demo
=====================================
A demonstration of the challenge system with visual effects.
"""

import time
import sys
from encoder import *

def typewriter_print(text, delay=0.03):
    """Print text with typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_slow(text, delay=0.5):
    """Print with a delay."""
    print(text)
    time.sleep(delay)

def demo_banner():
    """Display animated banner."""
    banner = """
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║     ███╗   ██╗██╗   ██╗██╗  ██╗                          ║
    ║     ████╗  ██║╚██╗ ██╔╝╚██╗██╔╝                          ║
    ║     ██╔██╗ ██║ ╚████╔╝  ╚███╔╝                           ║
    ║     ██║╚██╗██║  ╚██╔╝   ██╔██╗                           ║
    ║     ██║ ╚████║   ██║   ██╔╝ ██╗                          ║
    ║     ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝                          ║
    ║                                                           ║
    ║            SHADOW CIPHER CHALLENGE                        ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    """
    print(banner)
    time.sleep(1)

def demo_stage_1():
    """Demonstrate steganography stage."""
    print("\n" + "="*65)
    print(" STAGE 1: STEGANOGRAPHY DETECTION")
    print("="*65 + "\n")
    
    typewriter_print("Loading paragraph files...")
    time.sleep(0.5)
    
    with open('paragraph1.txt', 'r') as f:
        para1 = f.read()
    
    with open('paragraph2.txt', 'r', encoding='utf-8') as f:
        para2 = f.read()
    
    print(f"\n📄 paragraph1.txt: {len(para1)} bytes")
    print(f"📄 paragraph2.txt: {len(para2)} bytes")
    print(f"\n🔍 Size difference: {len(para2) - len(para1)} bytes")
    time.sleep(1)
    
    typewriter_print("\n🧐 Analyzing Unicode characters...")
    time.sleep(0.5)
    
    # Count zero-width chars
    zero_count = para2.count('\u200b')
    one_count = para2.count('\u2060')
    
    print(f"\n✓ Found {zero_count} Zero-Width Spaces (U+200B)")
    print(f"✓ Found {one_count} Word Joiners (U+2060)")
    time.sleep(1)
    
    typewriter_print("\n🔓 Extracting hidden binary data...")
    time.sleep(0.5)
    
    binary = ShadowEncoder.extract_binary(para2)
    print(f"\n✓ Extracted: {len(binary)} bits")
    print(f"📊 Binary preview: {binary[:50]}...")
    time.sleep(1.5)
    
    print("\n✅ STAGE 1 COMPLETE - Binary data extracted!")
    time.sleep(1)

def demo_stage_2():
    """Demonstrate binary conversion stage."""
    print("\n" + "="*65)
    print(" STAGE 2: BINARY ANALYSIS")
    print("="*65 + "\n")
    
    typewriter_print("Converting binary string to bytes...")
    time.sleep(0.5)
    
    with open('binary.txt', 'r') as f:
        binary_str = f.read()
    
    encrypted_bytes = BinaryObfuscator.from_binary_string(binary_str)
    
    print(f"\n✓ Converted to {len(encrypted_bytes)} bytes")
    print(f"🔢 Hex representation: {encrypted_bytes.hex()}")
    time.sleep(1)
    
    typewriter_print("\n🔬 Analyzing byte patterns...")
    time.sleep(0.5)
    
    print(f"\n📈 Byte distribution:")
    for i, byte in enumerate(encrypted_bytes):
        print(f"   Byte {i}: 0x{byte:02x} ({byte:3d}) {'█' * (byte // 10)}")
    time.sleep(1)
    
    print("\n🧩 Pattern suggests XOR encryption...")
    time.sleep(1)
    
    print("\n✅ STAGE 2 COMPLETE - Encryption detected!")
    time.sleep(1)

def demo_stage_3():
    """Demonstrate decryption stage."""
    print("\n" + "="*65)
    print(" STAGE 3: CRYPTANALYSIS & DECRYPTION")
    print("="*65 + "\n")
    
    typewriter_print("Reading key hint from flag.txt...")
    time.sleep(0.5)
    
    with open('flag.txt', 'r') as f:
        hint = f.read().strip()
    
    print(f"\n🔑 Key hint: {hint}")
    time.sleep(1)
    
    typewriter_print("\n🔐 Deriving encryption key...")
    time.sleep(0.5)
    
    print(f"   Round 1: SHA-256('{hint}')")
    time.sleep(0.3)
    print(f"   Round 2: SHA-256(hash)")
    time.sleep(0.3)
    print(f"   Round 3: SHA-256(hash)")
    time.sleep(0.3)
    
    key = XORCipher.derive_key(hint, rounds=3)
    print(f"\n✓ Key derived: {key.hex()[:32]}... ({len(key)} bytes)")
    time.sleep(1)
    
    typewriter_print("\n🔓 Applying XOR decryption...")
    time.sleep(0.5)
    
    with open('binary.txt', 'r') as f:
        binary_str = f.read()
    encrypted_bytes = BinaryObfuscator.from_binary_string(binary_str)
    
    decrypted = XORCipher.decrypt(encrypted_bytes, key)
    flag = decrypted.decode()
    
    # Animated flag reveal
    print("\n🎯 Decrypting", end="")
    for _ in range(5):
        print(".", end="", flush=True)
        time.sleep(0.3)
    print()
    
    time.sleep(0.5)
    print(f"\n{'='*65}")
    print(f"  🚩 FLAG RECOVERED: {flag}")
    print(f"{'='*65}\n")
    time.sleep(2)
    
    print("✅ STAGE 3 COMPLETE - Challenge solved!")
    time.sleep(1)

def demo_summary():
    """Display challenge summary."""
    print("\n" + "="*65)
    print(" CHALLENGE SUMMARY")
    print("="*65 + "\n")
    
    summary = """
    🔍 Techniques Demonstrated:
       ├─ Zero-width Unicode steganography
       ├─ Binary data extraction
       ├─ XOR cryptography
       └─ SHA-256 key derivation
    
    📊 Challenge Statistics:
       ├─ Difficulty: 8/10 (Hard)
       ├─ Stages: 3
       ├─ Data hidden: 88 bits
       └─ Encryption: Multi-round XOR
    
    🎓 Skills Required:
       ├─ Unicode analysis
       ├─ Binary manipulation
       ├─ Cryptographic understanding
       └─ Python scripting
    
    ✅ Challenge Verification:
       All stages completed successfully!
    """
    print(summary)
    
    time.sleep(1)
    
    print("="*65)
    print(" Thank you for watching the NYX Shadow Cipher demo!")
    print("="*65)
    print("\n Run 'python3 encoder.py' to try the challenge yourself!")
    print(" Or see WALKTHROUGH.md for complete solution details.\n")

def run_demo():
    """Run complete demonstration."""
    try:
        demo_banner()
        
        typewriter_print("\n🎬 Starting automated demonstration...\n", delay=0.05)
        time.sleep(1)
        
        demo_stage_1()
        input("\n⏸️  Press ENTER to continue to Stage 2...")
        
        demo_stage_2()
        input("\n⏸️  Press ENTER to continue to Stage 3...")
        
        demo_stage_3()
        input("\n⏸️  Press ENTER for summary...")
        
        demo_summary()
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Demo interrupted by user.")
        print("Run again with: python3 demo.py\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Demo error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_demo()
