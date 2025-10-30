import sys
input = lambda: sys.stdin.readline().rstrip()

X, Y, Z = map(int, input().split())
U, V, W = map(int, input().split())

result = (U // 100) * X + (V // 50) * Y + (W // 20) * Z
print(result)