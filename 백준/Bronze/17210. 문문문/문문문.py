n = int(input())
num = int(input())

if n > 5:
    print('Love is open door')

else:
    for i in range(n - 1):
        if num == 1:
            print(0)
            num = 0
        else:
            print(1)
            num = 1