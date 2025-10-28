import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
data = list(map(int, input().split()))

result = []
for i in range(n, 0, -1):
    result.insert(data[i - 1], i)

print(' '.join(map(str, result)))