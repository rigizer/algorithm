import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    s = input()
    if s == '0':
        break

    x = int(s)
    result = [str(x)]

    while x >= 10:
        p = 1
        for c in str(x):
            p *= int(c)

        x = p
        result.append(str(x))

    print(' '.join(result))