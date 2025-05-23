n, k = map(int, input().split())
count = 0

def func(path, x):
    global n, k, count
    if x == n:
        count += 1
        if count == k:
            print(path[:-1])
            exit(0)
        return
    elif x > n:
        return

    for i in range(1, 4):
        func(path + str(i) + '+', x + i)

func('', 0)
print(-1)