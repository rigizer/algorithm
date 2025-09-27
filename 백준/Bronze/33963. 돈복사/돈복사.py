import sys
input = lambda: sys.stdin.readline().rstrip()

n = input()
n_digit = len(n)
click = 0

while True:
    n = str(int(n) * 2)

    if n_digit < len(n):
        break
    else:
        click += 1

print(click)