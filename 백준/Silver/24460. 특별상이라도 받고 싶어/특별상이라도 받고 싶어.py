import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def solve(y, x, size):
    if size == 1:
        return board[y][x]

    half = size // 2
    candidates = [
        solve(y, x, half),
        solve(y, x + half, half),
        solve(y + half, x, half),
        solve(y + half, x + half, half)
    ]

    candidates.sort()
    return candidates[1]  # 두 번째로 작은 값

result = solve(0, 0, n)
print(result)