n = int(input())
a = sorted(map(int, input().split()))
result = count = 0
k = 2
for i in range((n + 1) // 2):
    while k - 1 < a[i]:
        count += 1
        k *= 2
    result += count
print(result+1)