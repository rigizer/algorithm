n, a, b = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]
result = 'HAPPY'
t = li[a - 1][b - 1]
if t < max([li[i][b - 1] for i in range(n)]) or t < max([li[a - 1][j] for j in range(n)]):
    result = 'ANGRY'
print(result)