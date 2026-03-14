import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    n = int(input())
    if n == 0:
        break

    grid = [input() for _ in range(n)]

    for i in range(n):
        cnt = 0
        result = []
        for j in range(n):
            if grid[i][j] == 'X':
                cnt += 1
            else:
                if cnt > 0:
                    result.append(cnt)
                    cnt = 0
        if cnt > 0:
            result.append(cnt)

        if result:
            print(' '.join(map(str, result)))
        else:
            print(0)

    for j in range(n):
        cnt = 0
        result = []
        for i in range(n):
            if grid[i][j] == 'X':
                cnt += 1
            else:
                if cnt > 0:
                    result.append(cnt)
                    cnt = 0
        if cnt > 0:
            result.append(cnt)

        if result:
            print(' '.join(map(str, result)))
        else:
            print(0)