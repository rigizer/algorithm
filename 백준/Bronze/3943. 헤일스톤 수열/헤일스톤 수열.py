import sys
input = lambda: sys.stdin.readline().rstrip()

result = []
t = int(input())
for _ in range(t):
    n = int(input())
    a = n

    while True:
        if n == 1:
            result.append(str(a))
            break

        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        a = max(a, n)

print('\n'.join(result))