n = int(input())
x = list(map(int, input().split()))

result = 0
for i, lemon in enumerate(x, 1):
    tmp = lemon - (n + 1 - i)
    result = max(result, tmp)
print(result)