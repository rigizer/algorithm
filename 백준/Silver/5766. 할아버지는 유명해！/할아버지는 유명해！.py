while True:
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break
    
    board = [list(map(int, input().split())) for _ in range(n)]
    score = {}
    result = []

    for i in range(n):
        for j in range(m):
            if score.get(board[i][j]) is None:
                score[board[i][j]] = 1
            else:
                score[board[i][j]] += 1
    
    _1st, _2nd = sorted(score.values(), reverse=True)[:2]
    for key, value in score.items():
        if value == _2nd:
            result.append(key)
    
    print(*sorted(result))