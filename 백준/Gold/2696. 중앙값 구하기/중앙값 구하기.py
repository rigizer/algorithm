import sys
input = lambda: sys.stdin.readline().rstrip()

import heapq

t = int(input())

for _ in range(t):
    m = int(input())
    
    nums = []
    while len(nums) < m:
        nums += list(map(int, input().split()))
    
    left = []
    right = []
    
    result = []
    
    for i in range(m):
        x = nums[i]
        
        if not left or x <= -left[0]:
            heapq.heappush(left, -x)
        else:
            heapq.heappush(right, x)
        
        if len(left) > len(right) + 1:
            heapq.heappush(right, -heapq.heappop(left))
        elif len(left) < len(right):
            heapq.heappush(left, -heapq.heappop(right))
        
        if i % 2 == 0:
            result.append(-left[0])
    
    print(len(result))
    
    for i in range(len(result)):
        if i % 10 == 9 or i == len(result) - 1:
            print(result[i])
        else:
            print(result[i], end=' ')