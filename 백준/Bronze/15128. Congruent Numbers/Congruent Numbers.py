p1, q1, p2, q2 = map(int, input().split())
result = p1 / q1 * p2 / q2 / 2
if int(result) == result:
    print(1)
else:
    print(0)