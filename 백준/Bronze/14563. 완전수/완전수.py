t = int(input())
n = list(map(int, input().split()))
for i in n:
    sum = 0
    for j in range(1, i):
        if i % j == 0:
            sum += j
    if sum == i:
        print('Perfect')
    elif sum > i:
        print('Abundant')
    else:
        print('Deficient')