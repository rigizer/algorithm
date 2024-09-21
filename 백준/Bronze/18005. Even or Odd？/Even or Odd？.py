n = int(input())
if n % 2:
    result = 0
elif n // 2 % 2 == 0:
    result = 2
else:
    result = 1
print(result)