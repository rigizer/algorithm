n, k = map(int, input().split())
data = {}
for _ in range(n):
    i = int(input())
    if i not in data.keys():
        data[i] = 1
    else:
        data[i] += 1
for i in data.keys():
    if data[i] % k != 0:
        print(i)
        break