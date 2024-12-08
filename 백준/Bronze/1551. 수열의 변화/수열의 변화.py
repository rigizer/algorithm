n, k = map(int, input().split())
a = list(map(int, input().split(',')))

for i in range(k):
    for j in range(len(a)-1):
        a.append(a[1]-a[0])
        a.pop(0)
    a.pop(0)

print(','.join(map(str, a)))