n = int(input())

if n == 2:
    a, b = map(int, input().split())
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            print(i)
if n == 3:
    a, b, c = map(int, input().split())
    for i in range(1, min(a, b, c) + 1):
        if a % i == 0 and b % i == 0 and c % i == 0:
            print(i)