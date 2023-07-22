li1 = [int(input()) for _ in range(3)]
li2 = [int(input()) for _ in range(3)]
a = li1[0] * 3 + li1[1] * 2 + li1[2]
b = li2[0] * 3 + li2[1] * 2 + li2[2]
if a == b:
    print('T')
elif a > b:
    print('A')
else:
    print('B')