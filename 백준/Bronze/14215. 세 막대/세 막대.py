data = sorted(map(int, input().split()))
result = data[0] + data[1] + min(data[2], data[0] + data[1] - 1)
print(result)