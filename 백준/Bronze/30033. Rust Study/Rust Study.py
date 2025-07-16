n = int(input())
page = list(map(int, input().split()))
study = list(map(int, input().split()))
result = 0
for i, j in zip(page, study):
    if i - j <= 0:
        result += 1
print(result)