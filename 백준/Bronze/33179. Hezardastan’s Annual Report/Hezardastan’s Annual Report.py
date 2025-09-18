import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
p = list(map(int, input().split()))

result = 0
for i in range(n):
    result += p[i] // 2 if p[i] % 2 == 0 else (p[i] // 2) + 1

print(result)