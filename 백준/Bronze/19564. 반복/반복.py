import sys
input = lambda: sys.stdin.readline().rstrip()

s = input()
result = 1
prev = -1
for ch in s:
    idx = ord(ch) - ord('a')
    if idx <= prev:
        result += 1
    prev = idx
print(result)