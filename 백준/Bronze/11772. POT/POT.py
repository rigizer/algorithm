n = int(input())
p = [int(input()) for _ in range(n)]
result = sum([(x // 10) ** (x % 10) for x in p])
print(result)