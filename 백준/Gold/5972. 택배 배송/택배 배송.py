import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    # 출발위치, 도착위치, 거리
    a, b, c = map(int, input().split())
    # 양방향 길이므로, a->b, b->a 둘 다 그래프 추가
    graph[a].append((b, c))
    graph[b].append((a, c))

dist = [1e9] * (n + 1)
# 1번 헛간부터 시작하기 때문에 자기 자신에 대해서는 거리 0으로 초기화
dist[1] = 0

# 시작점 1번에 대한 비용을 0으로 초기화
pq = [(0, 1)]
while pq:
    # 가장 적은 횟수의 누적 소 d를 우선으로 꺼냄
    d, u = heapq.heappop(pq)
    # 이미 더 짧은 경로가 있으면 무시 (다익스트라 최적화)
    if d != dist[u]:
        continue
    # n에 농부 찬홍이가 있기 때문에 n을 만나면 종료 (우선순위 큐 사용했기 때문)
    if u == n:
        break
    
    # 현재 헛간 u와 연결된 모든 헛간 v 확인
    for v, w in graph[u]:
        
        # u를 거쳐 v로 갈 때의 새로운 누적 비용 계산 (기존 누적 d, 새로운 거리 w)
        nd = d + w
        
        # 이전 비용보다 더 적은 누적된 소 갯수인 경우 갱신, 우선순위 큐에 대해 새롭게 등록
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

# n까지의 최소 소 출력
print(dist[n])