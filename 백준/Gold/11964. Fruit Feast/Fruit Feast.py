from collections import deque

t, a, b = map(int, input().split())

result = 0

queue = deque()
visited = [[False] * (t + 1) for _ in range(2)]
queue.append((0, False))
visited[False][0] = True

while queue:
    total, isWater = queue.popleft()

    result = max(result, total)

    if total + a <= t and not visited[isWater][total + a]:
        queue.append((total + a, isWater))
        visited[isWater][total + a] = True
    
    if total + b <= t and not visited[isWater][total + b]:
        queue.append((total + b, isWater))
        visited[isWater][total + b] = True
    
    if not isWater and not visited[isWater][round(total / 2)]:
        queue.append((round(total / 2), not isWater))
        visited[not isWater][round(total / 2)] = True
        
print(result)