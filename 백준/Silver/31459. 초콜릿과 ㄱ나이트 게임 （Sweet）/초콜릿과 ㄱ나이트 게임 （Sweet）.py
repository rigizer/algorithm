for _ in range(int(input())):
    x, y, nx, ny = map(int, input().split())
    visited = [[False] * x for _ in range(y)]

    result = 0
    for i in range(y):
        for j in range(x):
            if 0 <= i - ny and 0 <= j - nx and visited[i - ny][j - nx] == True:
                continue
            visited[i][j] = True
            result += 1
    
    print(result)