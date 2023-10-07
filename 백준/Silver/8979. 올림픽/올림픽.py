n, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
data.sort(key=lambda x:(-x[1], -x[2], -x[3], x[0]))
print(data[k - 1][0])