from itertools import combinations
import sys

def init_chickens(n, board):
    chickens = []
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                chickens.append((i, j))
    
    return chickens

def get_chicken_distance(n, board, chickens):
    distance = 0

    # 도시 탐색
    for i in range(n):
        for j in range(n):
            # 집이 있는 경우
            if board[i][j] == 1:
                min_chicken_distance = sys.maxsize
                
                for chicken in chickens:
                    # 치킨집(i, j)과 집(chicken[0], chicken[1]) 사이의 거리 계산
                    chicken_distance = abs(i - chicken[0]) + abs(j - chicken[1])
                    min_chicken_distance = min(min_chicken_distance, chicken_distance)
                
                distance += min_chicken_distance

    return distance

# N : N×N 크기의 도시
# M : 치킨집 M개 고르기
n, m = map(int, input().split())

# 0 : 빈 칸
# 1 : 집
# 2 : 치킨집
board = [list(map(int, input().split())) for _ in range(n)]

# 치킨집의 위치
chickens = init_chickens(n, board)

# 최소 치킨 거리
min_distance = sys.maxsize

# 치킨집 조합 구하기
# 순열 : 순서가 있는 조합 (중복 O)
# 조합 : 순서가 없는 조합 (중복 X)
for chicken in combinations(chickens, m):
    # chicken : M개씩 짝지은 치킨집들의 목록
    # M개의 치킨집을 선택한 경우의 치킨 거리 계산
    distance = get_chicken_distance(n, board, chicken)
    # 치킨 거리의 최소값 갱신
    min_distance = min(min_distance, distance)

print(min_distance)