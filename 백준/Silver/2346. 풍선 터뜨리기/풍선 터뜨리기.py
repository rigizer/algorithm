from collections import deque

n = int(input())
queue = deque(enumerate(map(int, input().split())))
ans = []

while queue:
    idx,num = queue.popleft()
    ans.append(idx + 1)
    if num > 0:
        queue.rotate(-(num-1))
    elif num < 0:
        queue.rotate(-num)
        
print(' '.join(map(str, ans)))