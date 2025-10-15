import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def init(h, w, board, visited):
    for i in range(h):
        for j in range(w):
            if board[i][j] == 'X':
                visited[i][j] = 'X'

def bfs(h, w, board):
    queue = deque()
    visited = [[' '] * w for _ in range(h)]

    init(h, w, board, visited)

    if board[0][0] == 'O':
        queue.append((0, 0))
        visited[0][0] = 'M'

    while queue:
        y, x = queue.popleft()

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if 0 <= ny < h and 0 <= nx < w and visited[ny][nx] == ' ':
                queue.append((ny, nx))
                visited[ny][nx] = 'M'
    
    print('+---' * w + '+')
    for i in range(h):
        for j in range(w):
            print('|', visited[i][j], '', end='')
        print('|')
        print('+---' * w + '+')

    if visited[h - 1][w - 1] == 'M':
        return True

    return False

t = int(input())
for case in range(1, t + 1):
    print('Case:', case)

    h, w = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    result = bfs(h, w, board)

    if result:
        print('Minions can cross the room')
    else:
        print('Minions cannot cross the room')