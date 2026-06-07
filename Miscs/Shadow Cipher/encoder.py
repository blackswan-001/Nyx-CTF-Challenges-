#!/usr/bin/env python3
"""
NYX CTF Challenge - Shadow Cipher System
=========================================
A multi-layered cryptographic puzzle combining steganography, 
custom encoding, and obfuscation techniques.

Warning: This challenge requires deep analysis and lateral thinking.
"""

import base64
import hashlib
import sys
from typing import List, Tuple

# ═══════════════════════════════════════════════════════════════
# STAGE 1: Zero-Width Steganography Engine
# ═══════════════════════════════════════════════════════════════

class ShadowEncoder:
    """
    Hides binary data in plain text using zero-width characters.
    Hint: Not all spaces are created equal...
    """
    
    # Zero-width characters for binary encoding
    ZERO = '\u200b'  # Zero Width Space (0)
    ONE = '\u2060'   # Word Joiner (1)
    
    @staticmethod
    def hide_binary(text: str, binary_data: str) -> str:
        """
        Embeds binary data using zero-width characters between words.
        Each bit is represented by a different invisible Unicode character.
        """
        words = text.split(' ')
        binary_cleaned = binary_data.replace(' ', '')
        
        if len(binary_cleaned) > len(words) - 1:
            raise ValueError("Text too short to hide binary data")
        
        result = []
        for i, word in enumerate(words):
            result.append(word)
            if i < len(binary_cleaned):
                if binary_cleaned[i] == '0':
                    result.append(ShadowEncoder.ZERO)
                elif binary_cleaned[i] == '1':
                    result.append(ShadowEncoder.ONE)
                result.append(' ')
            elif i < len(words) - 1:
                result.append(' ')
        
        return ''.join(result)
    
    @staticmethod
    def extract_binary(text: str) -> str:
        """
        Extracts hidden binary data from text containing zero-width chars.
        Returns binary string (e.g., '01001000').
        """
        binary = []
        for char in text:
            if char == ShadowEncoder.ZERO:
                binary.append('0')
            elif char == ShadowEncoder.ONE:
                binary.append('1')
        return ''.join(binary)


# ═══════════════════════════════════════════════════════════════
# STAGE 2: Custom XOR Cipher with Key Derivation
# ═══════════════════════════════════════════════════════════════

class XORCipher:
    """
    Multi-round XOR encryption with derived keys.
    Hint: The flag format holds secrets...
    """
    
    @staticmethod
    def derive_key(seed: str, rounds: int = 3) -> bytes:
        """
        Derives encryption key using iterative hashing.
        Each round builds upon the previous hash.
        """
        key = seed.encode()
        for _ in range(rounds):
            key = hashlib.sha256(key).digest()
        return key
    
    @staticmethod
    def encrypt(data: bytes, key: bytes) -> bytes:
        """
        XOR encryption with key cycling.
        """
        result = bytearray()
        for i, byte in enumerate(data):
            result.append(byte ^ key[i % len(key)])
        return bytes(result)
    
    @staticmethod
    def decrypt(data: bytes, key: bytes) -> bytes:
        """
        XOR decryption (same as encryption due to XOR properties).
        """
        return XORCipher.encrypt(data, key)


# ═══════════════════════════════════════════════════════════════
# STAGE 3: Obfuscated Binary Encoding
# ═══════════════════════════════════════════════════════════════

class BinaryObfuscator:
    """
    Converts data to binary with format obfuscation.
    Hint: Standard tools might not be enough...
    """
    
    @staticmethod
    def to_binary_string(data: bytes) -> str:
        """
        Converts bytes to space-separated binary octets.
        """
        return ' '.join(format(byte, '08b') for byte in data)
    
    @staticmethod
    def from_binary_string(binary_str: str) -> bytes:
        """
        Converts binary string back to bytes.
        """
        binary_cleaned = binary_str.replace(' ', '')
        if len(binary_cleaned) % 8 != 0:
            raise ValueError("Invalid binary string length")
        
        result = bytearray()
        for i in range(0, len(binary_cleaned), 8):
            byte = int(binary_cleaned[i:i+8], 2)
            result.append(byte)
        return bytes(result)


# ═══════════════════════════════════════════════════════════════
# STAGE 4: Flag Validator & Challenge Generator
# ═══════════════════════════════════════════════════════════════

class ChallengeSystem:
    """
    Main challenge orchestration system.
    """
    
    FLAG_PREFIX = "NYX{"
    FLAG_SUFFIX = "}"
    
    @staticmethod
    def create_challenge(flag: str, cover_text: str) -> Tuple[str, str]:
        """
        Creates a complete CTF challenge from a flag.
        
        Returns:
            (steganographic_text, encrypted_binary)
        """
        # Validate flag format
        if not flag.startswith(ChallengeSystem.FLAG_PREFIX):
            raise ValueError(f"Flag must start with {ChallengeSystem.FLAG_PREFIX}")
        
        # Extract flag content for key derivation
        flag_content = flag[len(ChallengeSystem.FLAG_PREFIX):].rstrip(ChallengeSystem.FLAG_SUFFIX)
        
        # Step 1: Derive encryption key from flag prefix
        key_seed = ChallengeSystem.FLAG_PREFIX.rstrip('{')
        encryption_key = XORCipher.derive_key(key_seed, rounds=3)
        
        # Step 2: Encrypt the flag
        encrypted_flag = XORCipher.encrypt(flag.encode(), encryption_key)
        
        # Step 3: Convert to binary representation
        binary_representation = BinaryObfuscator.to_binary_string(encrypted_flag)
        
        # Step 4: Hide binary in cover text using steganography
        stego_text = ShadowEncoder.hide_binary(cover_text, binary_representation)
        
        return stego_text, binary_representation
    
    @staticmethod
    def solve_challenge(stego_text: str, flag_prefix: str) -> str:
        """
        Solves the challenge by reversing all encoding steps.
        
        Args:
            stego_text: Text containing hidden data
            flag_prefix: Known flag prefix for key derivation
        
        Returns:
            Decrypted flag
        """
        # Step 1: Extract binary from steganographic text
        binary_data = ShadowEncoder.extract_binary(stego_text)
        
        # Step 2: Convert binary to bytes
        encrypted_bytes = BinaryObfuscator.from_binary_string(binary_data)
        
        # Step 3: Derive decryption key
        key_seed = flag_prefix.rstrip('{')
        decryption_key = XORCipher.derive_key(key_seed, rounds=3)
        
        # Step 4: Decrypt to recover flag
        decrypted_flag = XORCipher.decrypt(encrypted_bytes, decryption_key)
        
        return decrypted_flag.decode()
    
    @staticmethod
    def verify_flag(provided_flag: str, expected_flag: str) -> bool:
        """
        Verifies if the provided flag matches the expected flag.
        """
        return provided_flag.strip() == expected_flag.strip()


# ═══════════════════════════════════════════════════════════════
# INTERACTIVE CHALLENGE INTERFACE
# ═══════════════════════════════════════════════════════════════

def print_banner():
    """Displays challenge banner."""
    banner = """
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║           NYX SHADOW CIPHER CHALLENGE                     ║
    ║                                                           ║
    ║     "In darkness, only those who seek shall find"         ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    
    OBJECTIVE: Decode the hidden flag from the provided files
    
    FILES PROVIDED:
    ├── paragraph1.txt    (Clean reference text)
    ├── paragraph2.txt    (Something seems... different)
    ├── binary.txt        (Encrypted payload)
    └── flag.txt          (Partial information)
    
    HINTS:
    [1] Not all whitespace is visible to the eye
    [2] The flag format itself is part of the key
    [3] Multiple layers must be peeled like an onion
    [4] Binary representations can be deceiving
    
    DIFFICULTY: ████████░░ (8/10)
    """
    print(banner)


def interactive_mode():
    """
    Interactive mode for solving the challenge step by step.
    """
    print_banner()
    print("\n[*] Starting Interactive Challenge Mode\n")
    
    # Hint system
    hints = [
        "Compare paragraph1.txt and paragraph2.txt byte-by-byte",
        "Look for zero-width Unicode characters (U+200B, U+2060)",
        "The binary in binary.txt is XOR encrypted",
        "Use the flag prefix from flag.txt to derive the decryption key",
        "Key derivation uses SHA-256 with 3 rounds",
        "Final answer format: NYX{...}"
    ]
    
    hint_count = 0
    
    while True:
        print("\n" + "="*60)
        print("OPTIONS:")
        print("  [1] Get a hint")
        print("  [2] Validate flag")
        print("  [3] Show solution method")
        print("  [4] Exit")
        print("="*60)
        
        choice = input("\nEnter choice: ").strip()
        
        if choice == '1':
            if hint_count < len(hints):
                print(f"\n💡 HINT #{hint_count + 1}: {hints[hint_count]}")
                hint_count += 1
            else:
                print("\n⚠️  No more hints available!")
        
        elif choice == '2':
            user_flag = input("\nEnter the flag: ").strip()
            # This is just for demonstration - actual flag validation would be done
            print("\n🔍 Validating flag...")
            if user_flag.startswith("NYX{") and user_flag.endswith("}"):
                print("✓ Format correct! Now verify the content...")
            else:
                print("✗ Invalid flag format. Must be: NYX{...}")
        
        elif choice == '3':
            print("\n📖 SOLUTION METHOD:")
            print("""
            STEP 1: Compare paragraph1.txt and paragraph2.txt
                    → Extract zero-width characters
                    → Decode to binary string
            
            STEP 2: Analyze flag.txt for key material
                    → Use flag prefix "NYX" for key derivation
                    → Derive key: SHA-256("NYX", 3 rounds)
            
            STEP 3: Decrypt binary.txt using derived key
                    → Convert binary to bytes
                    → XOR decrypt with derived key
                    → Obtain final flag
            """)
        
        elif choice == '4':
            print("\n👋 Good luck, hacker!\n")
            break
        
        else:
            print("\n❌ Invalid choice!")


# ═══════════════════════════════════════════════════════════════
# COMMAND LINE INTERFACE
# ═══════════════════════════════════════════════════════════════

def main():
    """
    Main entry point with multiple operation modes.
    """
    if len(sys.argv) < 2:
        interactive_mode()
        return
    
    mode = sys.argv[1]
    
    if mode == '--create' and len(sys.argv) == 4:
        # Create new challenge
        flag = sys.argv[2]
        cover_text = sys.argv[3]
        
        try:
            stego_text, binary = ChallengeSystem.create_challenge(flag, cover_text)
            print("✓ Challenge created successfully!")
            print(f"\nSteganographic text:\n{stego_text}\n")
            print(f"Binary representation:\n{binary}\n")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    elif mode == '--solve' and len(sys.argv) == 4:
        # Solve existing challenge
        stego_text = sys.argv[2]
        flag_prefix = sys.argv[3]
        
        try:
            flag = ChallengeSystem.solve_challenge(stego_text, flag_prefix)
            print(f"✓ Flag recovered: {flag}")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    elif mode == '--extract' and len(sys.argv) == 3:
        # Extract binary from steganographic text
        stego_text = sys.argv[2]
        binary = ShadowEncoder.extract_binary(stego_text)
        print(f"Extracted binary:\n{binary}")
    
    elif mode == '--help':
        print("""
NYX Shadow Cipher - Usage Guide
================================

MODES:
  (no args)                     → Interactive challenge mode
  --create <flag> <text>        → Create new challenge
  --solve <stego_text> <prefix> → Solve challenge
  --extract <stego_text>        → Extract hidden binary
  --help                        → Show this help

EXAMPLES:
  python3 encoder.py
  python3 encoder.py --create "NYX{test_flag}" "Cover text here"
  python3 encoder.py --solve "..." "NYX"
  python3 encoder.py --extract "Text with hidden data"
        """)
    
    else:
        print("✗ Invalid arguments. Use --help for usage information.")


if __name__ == "__main__":
    main()
