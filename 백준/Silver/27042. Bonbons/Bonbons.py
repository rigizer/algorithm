import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

n = int(input())
queue = deque([i for i in range(1, n + 1)])

x = 0
while queue:
    a = queue.popleft()
    if x % 2 == 0:
        queue.append(a)
    x += 1

print(a)