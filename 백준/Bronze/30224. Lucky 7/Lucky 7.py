n = int(input())
s = str(n)

if '7' not in s and n % 7 != 0:
    print(0)
elif '7' not in s and n % 7 == 0:
    print(1)
elif '7' in s and n % 7 != 0:
    print(2)
else:
    print(3)