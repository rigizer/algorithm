import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = 10 ** 18

for i in range(n):
    s = arr[i] + arr[-1 - i]
    if s < result:
        result = s

print(result)