n, k = map(int, input().split())
placement = list(input())
result = 0
for j in range(n):
    if placement[j] == 'P':
        for i in range(max(j - k, 0), min(j + k + 1, n)):
            if placement[i] == 'H':
                placement[i] = 0
                result += 1
                break
print(result)