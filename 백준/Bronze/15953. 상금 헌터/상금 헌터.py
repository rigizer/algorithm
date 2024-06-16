first_place = [1, 3, 6, 10, 15, 21]
first_money = [500, 300, 200, 50, 30, 10]
second_place = [1, 3, 7, 15, 31]
second_money = [512, 256, 128, 64, 32]

for _ in range(int(input())):
    a_money = []
    b_money = []

    a, b = map(int, input().split())
    for f in first_place:
        if a > 21 or a == 0:
            a_money = [0]
        elif a <= f:
            a_money.append(first_money[first_place.index(f)])
        
    for s in second_place:
        if b > 31 or b == 0:
            b_money = [0]
        elif b <= s:
            b_money.append(second_money[second_place.index(s)])
    print((max(a_money) + max(b_money)) * 10000)