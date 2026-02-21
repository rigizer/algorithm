import sys
input = lambda: sys.stdin.readline().rstrip()

def digits_to_int(digits):
    value = 0
    for d in digits:
        value = value * 10 + d
    return value

t = int(input())
result = []

for _ in range(t):
    n, m = map(int, input().split())
    x_digits = list(map(int, input().split()))
    y_digits = list(map(int, input().split()))
    wheel = list(map(int, input().split()))

    x = digits_to_int(x_digits)
    y = digits_to_int(y_digits)

    count = 0
    for start in range(n):
        z = 0
        for k in range(m):
            z = z * 10 + wheel[(start + k) % n]
        if x <= z <= y:
            count += 1

    result.append(str(count))

for line in result:
    print(line)