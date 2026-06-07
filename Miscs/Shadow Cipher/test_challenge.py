#!/usr/bin/env python3
"""
NYX Challenge - Test Suite
===========================
Automated testing to ensure challenge integrity and solvability.
"""

import sys
import os
from encoder import *

class Colors:
    """ANSI color codes for terminal output."""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def print_header(text):
    """Print formatted section header."""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}{text:^60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.RESET}\n")

def print_success(text):
    """Print success message."""
    print(f"{Colors.GREEN}✓ {text}{Colors.RESET}")

def print_error(text):
    """Print error message."""
    print(f"{Colors.RED}✗ {text}{Colors.RESET}")

def print_info(text):
    """Print info message."""
    print(f"{Colors.YELLOW}ℹ {text}{Colors.RESET}")

def test_file_existence():
    """Test that all required files exist."""
    print_header("TEST 1: File Existence")
    
    required_files = [
        'encoder.py',
        'paragraph1.txt',
        'paragraph2.txt',
        'binary.txt',
        'flag.txt'
    ]
    
    all_exist = True
    for filename in required_files:
        if os.path.exists(filename):
            print_success(f"{filename} exists")
        else:
            print_error(f"{filename} missing")
            all_exist = False
    
    return all_exist

def test_file_integrity():
    """Test file content and encoding."""
    print_header("TEST 2: File Integrity")
    
    try:
        # Test paragraph1
        with open('paragraph1.txt', 'r', encoding='utf-8') as f:
            para1 = f.read()
            print_success(f"paragraph1.txt readable ({len(para1)} chars)")
        
        # Test paragraph2
        with open('paragraph2.txt', 'r', encoding='utf-8') as f:
            para2 = f.read()
            print_success(f"paragraph2.txt readable ({len(para2)} chars)")
        
        # Test size difference
        if len(para2) > len(para1):
            print_success(f"paragraph2 larger by {len(para2) - len(para1)} bytes (expected)")
        else:
            print_error("paragraph2 should be larger than paragraph1")
            return False
        
        # Test binary.txt
        with open('binary.txt', 'r') as f:
            binary = f.read()
            if '0' in binary and '1' in binary:
                print_success("binary.txt contains binary data")
            else:
                print_error("binary.txt doesn't contain valid binary")
                return False
        
        # Test flag.txt
        with open('flag.txt', 'r') as f:
            flag_hint = f.read().strip()
            if flag_hint == "NYX":
                print_success("flag.txt contains correct hint")
            else:
                print_error(f"flag.txt should contain 'NYX', found '{flag_hint}'")
                return False
        
        return True
    
    except Exception as e:
        print_error(f"File integrity check failed: {e}")
        return False

def test_steganography():
    """Test steganographic extraction."""
    print_header("TEST 3: Steganography Extraction")
    
    try:
        # Load files
        with open('paragraph2.txt', 'r', encoding='utf-8') as f:
            stego_text = f.read()
        
        # Extract binary
        extracted_binary = ShadowEncoder.extract_binary(stego_text)
        
        if extracted_binary:
            print_success(f"Extracted {len(extracted_binary)} bits")
            print_info(f"Binary preview: {extracted_binary[:40]}...")
        else:
            print_error("No binary data extracted")
            return False
        
        # Verify zero-width characters exist
        has_zero = '\u200b' in stego_text
        has_one = '\u2060' in stego_text
        
        if has_zero and has_one:
            print_success("Both zero-width character types detected")
        else:
            print_error("Missing zero-width characters")
            return False
        
        return True
    
    except Exception as e:
        print_error(f"Steganography test failed: {e}")
        return False

def test_binary_conversion():
    """Test binary to bytes conversion."""
    print_header("TEST 4: Binary Conversion")
    
    try:
        with open('binary.txt', 'r') as f:
            binary_str = f.read().strip()
        
        # Convert to bytes
        encrypted_bytes = BinaryObfuscator.from_binary_string(binary_str)
        
        if encrypted_bytes:
            print_success(f"Converted to {len(encrypted_bytes)} bytes")
            print_info(f"Hex: {encrypted_bytes.hex()}")
        else:
            print_error("Binary conversion failed")
            return False
        
        return True
    
    except Exception as e:
        print_error(f"Binary conversion test failed: {e}")
        return False

def test_key_derivation():
    """Test key derivation function."""
    print_header("TEST 5: Key Derivation")
    
    try:
        # Derive key from "NYX"
        key = XORCipher.derive_key("NYX", rounds=3)
        
        if len(key) == 32:  # SHA-256 produces 32 bytes
            print_success(f"Key derived successfully (32 bytes)")
            print_info(f"Key (hex): {key.hex()[:32]}...")
        else:
            print_error(f"Key length incorrect: {len(key)} bytes")
            return False
        
        # Test deterministic behavior
        key2 = XORCipher.derive_key("NYX", rounds=3)
        if key == key2:
            print_success("Key derivation is deterministic")
        else:
            print_error("Key derivation is not deterministic")
            return False
        
        return True
    
    except Exception as e:
        print_error(f"Key derivation test failed: {e}")
        return False

def test_decryption():
    """Test complete decryption process."""
    print_header("TEST 6: Decryption")
    
    try:
        with open('binary.txt', 'r') as f:
            binary_str = f.read().strip()
        
        # Convert to bytes
        encrypted_bytes = BinaryObfuscator.from_binary_string(binary_str)
        
        # Derive key
        key = XORCipher.derive_key("NYX", rounds=3)
        
        # Decrypt
        decrypted = XORCipher.decrypt(encrypted_bytes, key)
        flag = decrypted.decode()
        
        if flag.startswith("NYX{") and flag.endswith("}"):
            print_success(f"Flag decrypted: {flag}")
        else:
            print_error(f"Invalid flag format: {flag}")
            return False
        
        return True
    
    except Exception as e:
        print_error(f"Decryption test failed: {e}")
        return False

def test_complete_solution():
    """Test the complete end-to-end solution."""
    print_header("TEST 7: Complete Solution")
    
    try:
        # Load steganographic text
        with open('paragraph2.txt', 'r', encoding='utf-8') as f:
            stego_text = f.read()
        
        # Solve using challenge system
        recovered_flag = ChallengeSystem.solve_challenge(stego_text, "NYX")
        
        if recovered_flag:
            print_success(f"Challenge solved: {recovered_flag}")
            
            # Verify flag format
            if recovered_flag.startswith("NYX{") and recovered_flag.endswith("}"):
                print_success("Flag format is valid")
            else:
                print_error("Flag format is invalid")
                return False
            
            return True
        else:
            print_error("Failed to solve challenge")
            return False
    
    except Exception as e:
        print_error(f"Complete solution test failed: {e}")
        return False

def test_consistency():
    """Test consistency between different files."""
    print_header("TEST 8: Data Consistency")
    
    try:
        # Extract from paragraph2
        with open('paragraph2.txt', 'r', encoding='utf-8') as f:
            stego_text = f.read()
        extracted_binary = ShadowEncoder.extract_binary(stego_text)
        
        # Load from binary.txt
        with open('binary.txt', 'r') as f:
            binary_file = f.read().strip().replace(' ', '')
        
        # Compare
        if extracted_binary == binary_file:
            print_success("Extracted binary matches binary.txt")
        else:
            print_error("Binary mismatch between extraction and file")
            print_info(f"Extracted: {len(extracted_binary)} bits")
            print_info(f"File:      {len(binary_file)} bits")
            return False
        
        return True
    
    except Exception as e:
        print_error(f"Consistency test failed: {e}")
        return False

def run_all_tests():
    """Run complete test suite."""
    print(f"\n{Colors.BOLD}{Colors.BLUE}")
    print("╔════════════════════════════════════════════════════════════╗")
    print("║                                                            ║")
    print("║          NYX SHADOW CIPHER - TEST SUITE                    ║")
    print("║                                                            ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print(Colors.RESET)
    
    tests = [
        ("File Existence", test_file_existence),
        ("File Integrity", test_file_integrity),
        ("Steganography", test_steganography),
        ("Binary Conversion", test_binary_conversion),
        ("Key Derivation", test_key_derivation),
        ("Decryption", test_decryption),
        ("Complete Solution", test_complete_solution),
        ("Data Consistency", test_consistency),
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print_error(f"Test '{name}' crashed: {e}")
            results.append((name, False))
    
    # Summary
    print_header("TEST SUMMARY")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        if result:
            print_success(f"{name:<25} PASSED")
        else:
            print_error(f"{name:<25} FAILED")
    
    print(f"\n{Colors.BOLD}Results: {passed}/{total} tests passed{Colors.RESET}")
    
    if passed == total:
        print(f"\n{Colors.GREEN}{Colors.BOLD}🎉 ALL TESTS PASSED! Challenge is ready!{Colors.RESET}\n")
        return 0
    else:
        print(f"\n{Colors.RED}{Colors.BOLD}⚠️  Some tests failed. Please review.{Colors.RESET}\n")
        return 1

if __name__ == "__main__":
    sys.exit(run_all_tests())
