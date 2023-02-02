import heapq

# 노드의 개수 V, 간선의 개수 E
V, E = map(int, input().split())

# 시작 노드의 번호 (1 <= k <= V)
k = int(input())

# 그래프 초기화 (시작노드가 1부터 시작함에 따른 오차 보정)
# 어차피 0번 인덱스로 향하는 간선은 없음
graph = [[] for _ in range(V + 1)]

# 간선 E개 만큼 입력
for _ in range(E):
    # 노드 u에서 v로 가는 가중치가 w이다
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

# 최단거리를 저장할 수 있는 공간을 무한으로 초기화 (1e9)
distance = [1e9 for _ in range(V + 1)]

def dijkstra(start):
    # heapq(최소힙)를 사용하기 위한 리스트 초기화
    # 우선순위 큐(PriorityQueue)
    queue = []

    # 시작 노드 자기 자신에 대한 최단거리는 0으로 설정
    heapq.heappush(queue, (0, start)) # 우선순위 큐, (거리(우선순위), 노드번호))
    distance[start] = 0

    # 우선순위 큐 수행
    while queue:
        # 최단거리를 가지는 노드정보 탐색
        g, now = heapq.heappop(queue)

        # 현재 탐색중인 노드가 이미 처리된 적이 있는지 확인
        if distance[now] < g:
            continue
        
        # 현재 노드와 연결된 다른 인접 노드 확인
        for w, next in graph[now]:
            # next: 다음 노드 번호
            # next_w : 시작 노드부터 현재 노드까지의 거리(g) + 현재~다음 노드까지의 거리(w)
            next_w = g + w

            # [시작 노드부터 다음 노드까지의 거리]가 [지금 기록된 거리]보다 더 최단거리인지 확인
            if next_w < distance[next]:
                # next 정점까지의 거리에 대해 최단거리 갱신
                distance[next] = next_w

                # 다음 정점에 대해 최단거리 탐색
                heapq.heappush(queue, (next_w, next))
            
# 시작번호 k부터 시작하는 다익스트라 최단거리 알고리즘 수행
dijkstra(k)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, V + 1):
    # 최단거리를 구하지 못한 경우 INF, 최단거리가 있으면 해당 거리 출력
    print('INF' if distance[i] == 1e9 else distance[i])