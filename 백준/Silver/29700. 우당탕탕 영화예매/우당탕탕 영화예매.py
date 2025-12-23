import sys
input = lambda: sys.stdin.readline().rstrip()

n, m, k = map(int, input().split())
result = 0

for _ in range(n):
    row = input()
    cnt = 0
    for c in row:
        if c == '0':
            cnt += 1
        else:
            if cnt >= k:
                result += cnt - k + 1
            cnt = 0
    if cnt >= k:
        result += cnt - k + 1

print(result)