n = int(input())
temp = dict()

for _ in range(n):
    a, b = map(str, input().split())

    if b == 'enter':
        temp[a] = b
    else:
        del temp[a]

temp = sorted(temp.keys(), reverse=True)

for i in temp:
    print(i)