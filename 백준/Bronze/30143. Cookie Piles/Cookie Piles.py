import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    n, a, d = map(int, input().split())
    result = (n * (2 * a + (n - 1) * d)) // 2
    print(result)