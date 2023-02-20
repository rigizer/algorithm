from collections import deque

queue = deque()

# N : 키를 비교해야 하는 학생들의 수
# M : 키를 비교한 횟수
n, m = map(int, input().split())

# 방문여부 초기화
visited = [False for _ in range(n + 1)]

# 진입차수 초기화
indegree = [0 for _ in range(n + 1)]

# 그래프 초기화
graph = [[] for _ in range(n + 1)]

# 데이터 입력
for _ in range(m):
    front, back = map(int, input().split())
    graph[front].append(back)
    indegree[back] += 1

# 진입차수가 0인 노드 탐색
for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)
        visited[i] = True

result = []
while queue:
    now = queue.popleft()
    result.append(now)

    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            queue.append(i)

print(' '.join(str(i) for i in result))