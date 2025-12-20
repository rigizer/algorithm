import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    tickets = list(map(int, input().split()))
    count = [0] * (n + 1)

    for t in tickets:
        count[t] += 1

    result = 0
    for i in range(1, n + 1):
        if count[i] >= 2:
            result += 1

    print(result)