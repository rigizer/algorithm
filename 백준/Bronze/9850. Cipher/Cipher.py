import sys
input = lambda: sys.stdin.readline().rstrip()

cipher = input()

def decrypt_char(c, p):
    if 'A' <= c <= 'Z':
        return chr((ord(c) - ord('A') - p) % 26 + ord('A'))
    return c

for p in range(26):
    decrypted = ''.join(decrypt_char(c, p) for c in cipher)
    if 'CHIPMUNKS' in decrypted and 'LIVE' in decrypted:
        print(decrypted)
        break