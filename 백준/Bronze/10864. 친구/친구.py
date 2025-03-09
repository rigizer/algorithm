n, m = map(int, input().split())
cnt = []
for i in range(m):
    a, b = map(int, input().split())
    cnt.append(a)
    cnt.append(b)
 
for i in range(1, n + 1):
    print(cnt.count(i))