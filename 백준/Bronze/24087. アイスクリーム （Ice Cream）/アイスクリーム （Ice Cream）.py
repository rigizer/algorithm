s, a, b = int(input()), int(input()), int(input())
if s <= a: print(250)
else:
    print (250 + ((s - a) // b) * 100 if ((s - a) // b) == ((s - a) / b) else 250 + ((s - a) // b + 1) * 100)