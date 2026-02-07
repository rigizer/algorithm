import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
half = m // 2

for _ in range(n):
    row = list(input())
    result = ['.'] * m
    for j in range(half):
        k = m - 1 - j
        x = row[j] if row[j] != '.' else row[k]
        result[j] = x
        result[k] = x
    print(''.join(result))