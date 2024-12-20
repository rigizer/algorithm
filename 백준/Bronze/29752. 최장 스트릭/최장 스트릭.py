n = int(input())
data = list(map(int, input().split()))
result = 0
max_result = 0

for i in data:
    if i == 0:
        result = 0
        continue
    result += 1
    max_result = max(result, max_result)

print(max_result)