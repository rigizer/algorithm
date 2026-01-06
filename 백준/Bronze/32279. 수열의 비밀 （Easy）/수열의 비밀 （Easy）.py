import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
p, q, r, s = map(int, input().split())
a1 = int(input())

a = [0] * (n + 1)
a[1] = a1

result = a1

for i in range(2, n + 1):
    if i % 2 == 0:
        a[i] = p * a[i // 2] + q
    else:
        a[i] = r * a[i // 2] + s
    result += a[i]

print(result)