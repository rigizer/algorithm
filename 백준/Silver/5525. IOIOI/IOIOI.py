import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
m = int(input())
s = input()

result = 0

for i in range(m - (2 * n)):
    if s[i: i + 2 * n + 1] == 'IO' * n + 'I':
        result += 1

print(result)