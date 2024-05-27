from collections import deque

def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        queue.append((x, y))

def bfs():
    while queue:
        x, y = queue.popleft()
        z = c - x - y

        if x == 0:
            answer.append(z)

        water = min(x, b-y)
        pour(x - water, y + water)
        
        water = min(x, c-z)
        pour(x - water, y)
        
        water = min(y, a-x)
        pour(x + water, y - water)
        
        water = min(y, c-z)
        pour(x, y - water)
        
        water = min(z, a-x)
        pour(x + water, y)
        
        water = min(z, b-y)
        pour(x, y + water)


a, b, c = map(int, input().split())

queue = deque()
queue.append((0, 0))

visited = [[False] * (b + 1) for _ in range(a + 1)]
visited[0][0] = True

answer = []

bfs()

answer.sort()
for i in answer:
    print(i, end=' ')