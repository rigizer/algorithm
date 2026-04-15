import sys
input = lambda: sys.stdin.readline().rstrip()

arr = list(map(int, input().split()))
n, kwf = map(int, input().split())

total = 0
for i in range(0, 10, 2):
    total += arr[i] * arr[i + 1]

avg = total // 5
result = (avg * n) // kwf

print(result)