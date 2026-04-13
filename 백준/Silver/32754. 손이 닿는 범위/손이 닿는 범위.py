import sys
input = lambda: sys.stdin.readline().rstrip()

import math

n, R = map(int, input().split())
result = 0

for _ in range(n):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    
    cx = (x1 + x2 + x3 + x4) / 4
    cy = (y1 + y2 + y3 + y4) / 4
    
    dx = cx
    dy = cy
    dist_c = math.hypot(dx, dy)
    
    r = math.hypot(x1 - cx, y1 - cy)
    
    if dist_c - r <= R:
        result += 1

print(result)