t = int(input())
for _ in range(t):
    n, k, t, m = map(int, input().split())
    board = [[0] * k for _ in range(n)]
    count = [0] * n
    time = [0] * n
    for ts in range(m):
        i, j, s = map(int, input().split())
        board[i - 1][j - 1] = max(board[i - 1][j - 1], s)
        count[i - 1] += 1
        time[i - 1] = ts
    data = []
    for idx in range(n):
        data.append([sum(board[idx]), count[idx], time[idx], idx])
    data.sort(key=lambda x: (-x[0], x[1], x[2]))
    for idx in range(n):
        if data[idx][3] == t - 1:
            print(idx + 1)
            break