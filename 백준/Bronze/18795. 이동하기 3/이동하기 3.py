import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = sum(a) + sum(b)
print(result)