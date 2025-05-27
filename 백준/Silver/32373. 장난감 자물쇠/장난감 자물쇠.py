def calc(n, k, a):
    groups = {}
    for i in range(n):
        r = i % k
        if r not in groups:
            groups[r] = []
        groups[r].append(a[i])

    for r in groups:
        groups[r].sort()

    sorted_arr = [0] * n
    indices = {r: 0 for r in groups}

    for i in range(n):
        r = i % k
        sorted_arr[i] = groups[r][indices[r]]
        indices[r] += 1

    return sorted_arr == sorted(a)

n, k = map(int, input().split())
a = list(map(int, input().split()))

result = calc(n, k, a)
print('Yes' if result else 'No')