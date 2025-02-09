tc = int(input())
for _ in range(tc):
    r, e, c = map(int, input().split())
    if r > e - c:
        print('do not advertise')
    elif r == e - c:
        print('does not matter')
    else:
        print('advertise')