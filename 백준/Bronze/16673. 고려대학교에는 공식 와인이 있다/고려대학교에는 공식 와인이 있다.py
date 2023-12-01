c, k, p = map(int, input().split())
data = [k * i + p * (i ** 2) for i in range(1, c+1)]
print(sum(data))