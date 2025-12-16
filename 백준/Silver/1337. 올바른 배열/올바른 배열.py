import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = [int(input()) for _ in range(N)]

arr.sort()

max_count = 0
l = 0

for r in range(N):
    while arr[r] - arr[l] > 4:
        l += 1
    current_count = r - l + 1
    if current_count > max_count:
        max_count = current_count

result = 5 - max_count
if result < 0:
    result = 0

print(result)