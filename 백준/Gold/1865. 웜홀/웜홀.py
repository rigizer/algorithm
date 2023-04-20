# https://www.acmicpc.net/problem/1865
# 벨만-포드, 그래프

def bellman_ford(n, graph, distance):
    # 시작 지점을 1로 지정, 거리 초기화
    distance[1] = 0

    # 음의 사이클 판별 위해 n번 반복
    for i in range(n):
        # 반복시 모든 간선 확인
        for v in range(1, n + 1):
            for next_v, next_g in graph[v]:
                # 다음 노드로 이동하는 거리가 최단거리로 갱신 가능한 경우
                if distance[next_v] > distance[v] + next_g:
                    distance[next_v] = distance[v] + next_g

                    # 음의 사이클이 발생한 경우
                    if i == n - 1:
                        return False
    
    # 출발 위치로 아무런 이상없이 온 경우
    return True

tc = int(input())
for _ in range(tc):
    # n: 지점의 수, m: 도로의 수, w: 웜홀의 개수
    n, m, w = map(int, input().split())

    # 각 지점은 1부터 시작
    graph = [[] for _ in range(n + 1)]

    # 최단거리 초기화
    distance = [2e9] * (n + 1)

    # 도로의 간선정보 입력 (도로에는 방향이 없음, 양방향)
    for i in range(m):
        s, e, t = map(int, input().split())
        graph[s].append((e, t))
        graph[e].append((s, t))
    
    # 웜홀의 간선정보 입력 (시작 위치에서 도착 위치로 가는 하나의 경로)
    for _ in range(w):
        s, e, t = map(int, input().split())
        graph[s].append((e, -t))

    if bellman_ford(n, graph, distance):
        print('NO')
    else:
        print('YES')