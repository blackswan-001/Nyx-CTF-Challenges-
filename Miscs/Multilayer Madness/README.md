# Multi-Layer Encoding Challenge

## Challenge Description
You've intercepted an encoded transmission. Your mission: decode it through 5 layers of obfuscation to retrieve the flag.

## Files Provided
- `challenge.txt` - The intercepted transmission
- `layer5_dup.txt` - Reference: Duplicated binary

## Your Task
Decode the binary data in `challenge.txt` by reversing these operations:
1. Remove duplication (each bit appears twice)
2. Convert binary to ASCII characters
3. Reverse the string
4. Decode Base85
5. XOR with the key from `layer1_xor.bin`

## Hints
- The layer files show intermediate states to help you understand the encoding
- Start with the binary data in challenge.txt
- Work backwards through the layers
- The XOR key length matches the flag length

## Flag Format
`NYX{...}`

Good luck, Agent!