import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
pages = 0
i = 0
while i < n:
    pages += 1
    j = i + 1
    while j < n and arr[j] < 2 * arr[i]:
        j += 1
    i = j
print(pages)