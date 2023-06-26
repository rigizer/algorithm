lst = sorted(list(map(int, input().split())))
 
if lst[0] == lst[1]:
    print('S')
elif lst[1] == lst[2]:
    print('S')
elif lst[0]+lst[1] == lst[2]:
    print('S')
else:
    print('N')