n = int(input())
for i in range(n):
    s = int(input())
    for j in range(2, 1000001):
        if s % j == 0:
            print('NO')
            break
        if j == 1000000:
            print('YES')