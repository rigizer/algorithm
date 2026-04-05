import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    result = 0
    for i in range(1, n + 1):
        result = (result + m) % i

    print(result + 1)