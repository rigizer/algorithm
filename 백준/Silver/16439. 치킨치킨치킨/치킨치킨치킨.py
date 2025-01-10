from itertools import combinations

n, m = map(int, input().split())
like = [list(map(int, input().split())) for _ in range(n)]

max_sum = 0
for a, b, c in combinations(range(m), 3):
    tmp_sum = 0
    for i in range(n):
        tmp_sum += max(like[i][a], like[i][b], like[i][c])
    max_sum = max(max_sum, tmp_sum)

print(max_sum)