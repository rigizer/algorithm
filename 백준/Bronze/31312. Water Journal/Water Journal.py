n, a, b = map(int, input().split())
logs = [int(input()) for _ in range(n - 1)]

min_exist = a in logs
max_exist = b in logs

result = []

for x in range(a, b + 1):
    if (min_exist or x == a) and (max_exist or x == b):
        result.append(x)

if result:
    print('\n'.join([str(i) for i in result]))
else:
    print(-1)