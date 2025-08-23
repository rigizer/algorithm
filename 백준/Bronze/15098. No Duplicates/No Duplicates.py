w = list(map(str, input().split()))
d = dict()

for i in w:
    a = d.get(i, 0)
    if a == 0:
        d[i] = 1
    else:
        print('no')
        exit(0)
print('yes')