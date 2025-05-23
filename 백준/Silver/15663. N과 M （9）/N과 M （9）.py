n, m = map(int, input().split())
data = sorted(list(map(int, input().split())))
result = []
visited = [False] * n

def func(path):
    if len(path) == m:
        result.append(tuple(path))
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            func(path + [data[i]])
            visited[i] = False

func([])

result = sorted(set(result))
for i in result:
    print(*i)