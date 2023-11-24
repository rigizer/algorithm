tc = int(input())
price = [350.34, 230.90, 190.55, 125.30, 180.90]

for _ in range(tc) :
    sum = 0
    data = list(map(float, input().split()))
    for i in range(5) :
        sum += price[i] * data[i]

    print("$%.2f" % sum)