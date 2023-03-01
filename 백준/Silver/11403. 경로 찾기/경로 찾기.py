# 데이터 입력
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 플로이드-워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

# 데이터 출력
for g in graph:
    print(*g)