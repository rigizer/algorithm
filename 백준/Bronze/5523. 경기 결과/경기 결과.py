a = b = 0
for _ in range(int(input())):
    A, B = map(int, input().split())
    if A > B:
        a += 1
    elif A < B:
        b += 1
print(a, b)