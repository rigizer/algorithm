n, m = map(int, input().split())
k = list(map(int, input().split()))
r = 0
for i in range(1, n + 1):
    for n in k:
        if i % n == 0:
            r += i
            break
print(r)