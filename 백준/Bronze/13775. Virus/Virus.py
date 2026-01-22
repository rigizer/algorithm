import sys
input = lambda: sys.stdin.readline().rstrip()

k = int(input())
s = input()

result = []
shift = k

for c in s:
    if 'a' <= c <= 'z':
        x = ord(c) - ord('a')
        x = (x - shift) % 26
        result.append(chr(x + ord('a')))
        shift += 1
        if shift == 26:
            shift = 1
    else:
        result.append(c)

print(''.join(result))