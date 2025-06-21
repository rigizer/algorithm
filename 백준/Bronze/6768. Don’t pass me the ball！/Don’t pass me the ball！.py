j = int(input())
if j < 4:
    print(0)
else:
    n = j - 1
    result = n * (n - 1) * (n - 2) // 6
    print(result)