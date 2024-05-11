global_ponix = [input() for _ in range(3)]
l = k = p = False

for i in global_ponix:
    if i[0] == 'l':
        l = True
    elif i[0] == 'k':
        k = True
    elif i[0] == 'p':
        p = True

print('GLOBAL' if l == k == p == True else 'PONIX')