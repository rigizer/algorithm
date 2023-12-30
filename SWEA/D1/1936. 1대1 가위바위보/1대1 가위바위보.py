a, b = map(int, input().split())
if a == 1:
    if b == 2:
        print('B')
    elif b == 3:
        print('A')
elif a == 2:
    if b == 1:
        print('A')
    elif b == 3:
        print('B')
elif a == 3:
    if b == 1:
        print('B')
    elif b == 2:
        print('A')