import sys
input = lambda: sys.stdin.readline().rstrip()
from bisect import bisect_left, bisect_right

n, q = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

result = []

for _ in range(q):
    a, b = map(int, input().split())
    
    left = bisect_left(arr, a)
    right = bisect_right(arr, b)
    
    result.append(str(right - left))

print('\n'.join(result))