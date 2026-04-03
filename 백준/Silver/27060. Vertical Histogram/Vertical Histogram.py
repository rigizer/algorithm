import sys
input = lambda: sys.stdin.readline().rstrip()

cnt = [0] * 26

for _ in range(4):
    s = input()
    for ch in s:
        if 'A' <= ch <= 'Z':
            cnt[ord(ch) - ord('A')] += 1

max_h = max(cnt)

result = []

for h in range(max_h, 0, -1):
    line = []
    for i in range(26):
        if cnt[i] >= h:
            line.append('*')
        else:
            line.append(' ')
    while line and line[-1] == ' ':
        line.pop()
    result.append(' '.join(line))

alphabet = ' '.join(chr(ord('A') + i) for i in range(26))
result.append(alphabet)

print('\n'.join(result))