from collections import deque

def bfs():
    queue = deque()
    visited = [False] * 101

    queue.append((1, 0))
    visited[1] = True

    while queue:
        nx, nt = queue.popleft()

        if nx == 100:
            return nt

        # 1 ~ 6까지
        for d in range(1, 7):
            x = nx + d

            # 사다리 혹은 뱀과 연결된 경우
            for start, end in ladder:
                if x == start and visited[x] == False:
                    queue.append((end, nt + 1))
                    visited[end] = True
                    visited[x] = True
            
            # 사다리 혹은 뱀에 연결되지 않은 경우
            else:
                if 1 <= x <= 100 and visited[x] == False:
                    queue.append((x, nt + 1))
                    visited[x] = True

n, m = map(int, input().split())
ladder = [list(map(int, input().split())) for _ in range(n + m)]

result = bfs()
print(result)