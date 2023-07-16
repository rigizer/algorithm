k = int(input())
fee = 25 + k * 0.01

if fee < 100:
    print(100)
elif fee > 2000:
    print(2000)
else:
    print(fee)