def leap(year):
    if year % 4 == 0:
        if year % 400 != 0 and year % 100 == 0:
            return [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            return [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        return [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    d, m, y = map(int, input().split())
    if (m,d,y) == (0,0,0):
        break
    li = leap(y)
    print(sum(li[:m])+d)