import sys
input = lambda: sys.stdin.readline().rstrip()

t = input()
known = 'CHICKENS'

key = ord(t[0]) ^ ord(known[0])

result = []
for ch in t:
    result.append(chr(ord(ch) ^ key))

print(''.join(result))