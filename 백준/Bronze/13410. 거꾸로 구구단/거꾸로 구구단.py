n, k = map(int, input().split())

r = 0
for i in range(1, k + 1):
    r = max(r, int(str(n * i)[::-1]))

print(r)