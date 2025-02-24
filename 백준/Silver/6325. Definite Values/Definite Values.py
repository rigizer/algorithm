num = 0
while True:
    n = int(input())
    if n == 0: break
    elif num != 0: print()

    data = {'a': 1}
    for _ in range(n):
        temp = list(input().split())
        x, y = temp[0], temp[2]

        if y in data.keys():
            data[x] = data.get(y)
        elif x in data.keys() and y not in data.keys():
            data.pop(x)
    
    num += 1
    print(f'Program #{num}')

    if len(data.keys()) == 0:
        print('none')
    else:
        print(*sorted(data.keys()))