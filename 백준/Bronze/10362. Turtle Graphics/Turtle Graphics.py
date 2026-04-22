import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())

for tc in range(1, t + 1):
    x, y = map(int, input().split())
    cmds = input()

    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    d = 0

    visited = {}
    visited[(x, y)] = 1

    result = 0

    for c in cmds:
        if c == 'F':
            x += dx[d]
            y += dy[d]
            if (x, y) in visited:
                visited[(x, y)] += 1
                if visited[(x, y)] == 2:
                    result += 1
            else:
                visited[(x, y)] = 1
        elif c == 'R':
            d = (d + 1) % 4
        else:
            d = (d + 3) % 4

    print(f'Case #{tc}: {x} {y} {result}')