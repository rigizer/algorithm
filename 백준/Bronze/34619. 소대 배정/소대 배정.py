import sys
input = lambda: sys.stdin.readline().rstrip()

a, b, n, k = map(int, input().split())
k -= 1

i = b * n
x = k // i
y = (k - (x * i)) // n

print(x + 1, y + 1)