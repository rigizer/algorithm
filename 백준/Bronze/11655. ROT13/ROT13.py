import sys
input = lambda: sys.stdin.readline().rstrip()

s = input()
result = []
for ch in s:
    if 'a' <= ch <= 'z':
        result.append(chr((ord(ch) - ord('a') + 13) % 26 + ord('a')))
    elif 'A' <= ch <= 'Z':
        result.append(chr((ord(ch) - ord('A') + 13) % 26 + ord('A')))
    else:
        result.append(ch)

print(''.join(result))