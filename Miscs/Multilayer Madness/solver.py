#!/usr/bin/env python3
"""
Multi-Layer Challenge Solver
Decodes the challenge.txt through 5 layers
"""

import base64

def solve_challenge():
    print("="*70)
    print("MULTI-LAYER CHALLENGE SOLVER")
    print("="*70)
    
    # Read the encoded binary from challenge.txt
    with open('challenge.txt', 'r') as f:
        content = f.read()
        # Extract binary after the dashes
        binary_data = content.split('---------------------------------------------')[1].strip()
        binary_data = binary_data.replace('\n', '').replace(' ', '')
    
    print(f"\nStep 1: Read binary data")
    print(f"Length: {len(binary_data)} bits")
    
    # Layer 5: Remove duplication (each bit appears twice)
    print(f"\nStep 2: Remove duplication")
    deduplicated = ""
    i = 0
    while i < len(binary_data):
        char = binary_data[i]
        if i + 1 < len(binary_data) and binary_data[i+1] == char:
            deduplicated += char
            i += 2
        else:
            deduplicated += char
            i += 1
    
    print(f"Deduplicated length: {len(deduplicated)} bits")
    
    # Layer 4: Convert binary to bytes
    print(f"\nStep 3: Convert binary to bytes")
    binary_bytes = bytearray()
    for i in range(0, len(deduplicated), 8):
        byte = deduplicated[i:i+8]
        if len(byte) == 8:
            binary_bytes.append(int(byte, 2))
    
    binary_bytes = bytes(binary_bytes)
    b85_string = binary_bytes.decode('ascii')
    print(f"Decoded to ASCII: {len(binary_bytes)} bytes")
    
    # Layer 3: Reverse
    print(f"\nStep 4: Reverse the string")
    reversed_string = b85_string[::-1]
    print(f"Reversed: {reversed_string[:50]}...")
    
    # Layer 2: Base85 decode
    print(f"\nStep 5: Decode Base85")
    decoded = base64.b85decode(reversed_string)
    print(f"Decoded: {len(decoded)} bytes")
    
    # Layer 1: XOR with key
    print(f"\nStep 6: XOR with key")
    with open('layer1_xor.bin', 'rb') as f:
        xor_key = f.read()
    
    result = bytearray()
    for i in range(len(decoded)):
        result.append(decoded[i] ^ xor_key[i])
    
    flag = bytes(result).decode('utf-8')
    
    print(f"\n{'='*70}")
    print(f"FLAG FOUND: {flag}")
    print(f"{'='*70}")
    
    # Verify
    with open('flag.txt', 'r') as f:
        expected = f.read().strip()
    
    if flag == expected:
        print(f"\n✓ SUCCESS! Flag is correct!")
    else:
        print(f"\n✗ Flag mismatch. Expected: {expected}")
    
    return flag

if __name__ == '__main__':
    solve_challenge()
