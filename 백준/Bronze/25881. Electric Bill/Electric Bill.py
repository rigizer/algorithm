a, b = map(int, input().split())
for _ in range(int(input())) :
    p = int(input())
    result = a * [1000, p][p <= 1000]
    if p > 1000 :
        result += (p - 1000) * b
    print(p, result)