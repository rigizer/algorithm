ab = input()
size = len(ab)

if size == 2:
    a = int(ab[0])
    b = int(ab[1])

elif size == 3:
    if ab[0:2] == '10':
        a = 10
        b = int(ab[2])
    else:
        a = int(ab[0])
        b = 10

elif size == 4:
    a = 10
    b = 10

print(a + b)