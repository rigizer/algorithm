n, l = map(int,input().split())
h = sorted(list(map(int, input().split())))
for i in h:
    if i <= l:
        l += 1
print(l)