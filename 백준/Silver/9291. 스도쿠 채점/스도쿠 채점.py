import sys
input = lambda: sys.stdin.readline().rstrip()

is_valid_sudoku = lambda t: all(
    len(set(t[i])) == 9 and
    len(set(t[j][i] for j in range(9))) == 9 and
    len({t[3*(i//3)+k][3*(i%3)+l] for k in range(3) for l in range(3)}) == 9
    for i in range(9)
)

n = int(input())
results = []
for case in range(1, n + 1):
    table = [list(map(int, input().split())) for _ in range(9)]
    if case < n:
        input()
    results.append(f"Case {case}: {'CORRECT' if is_valid_sudoku(table) else 'INCORRECT'}")

print('\n'.join(results))