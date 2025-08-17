n, m = map(int, input().split())
data = sorted(list(map(int, input().split())))
result = []

def func(start, path):
    if len(path) == m:
        result.append(tuple(path))
        return

    for i in range(start, n):
        func(i + 1, path + [data[i]])

func(0, [])

result = sorted(set(result))
for i in result:
    print(*i)