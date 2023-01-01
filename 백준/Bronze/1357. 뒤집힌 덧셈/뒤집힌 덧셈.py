x, y = input().split()
result = int(x[::-1]) + int(y[::-1])
print(int(str(result)[::-1]))