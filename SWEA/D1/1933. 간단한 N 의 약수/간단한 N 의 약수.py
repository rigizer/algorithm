import math

n = int(input())
data = []
for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        data.append(i)

data2 = []
for i in data:
    data2.append(n // i)

data.extend(reversed(data2))
print(*data)