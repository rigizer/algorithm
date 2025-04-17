n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sum = 0
for i in range(0, n) :
    sum += abs(a[i] - b[i])

print(sum // 2)