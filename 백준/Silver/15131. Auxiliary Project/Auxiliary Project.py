import sys

n = int(sys.stdin.readline())

q = n // 3
r = n % 3

if r == 0:
    print(q * 7)
elif r == 1:
    print((q - 1) * 7 + 4)
else:
    print(q * 7 + 1)