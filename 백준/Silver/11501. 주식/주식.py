t = int(input())
for t in range(t):
    n = int(input())
    price = list(map(int, input().split()))

    money = 0
    max_price = 0
    for i in range(len(price)-1, -1, -1):
        if price[i] > max_price:
            max_price = price[i]
        else:
            money += max_price - price[i]

    print(money)