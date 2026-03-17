k = int(input())
n = int(input())

total = 0
for i in range(1, n):
    print(i)
    total += i

print(k - total)