n, k = map(int, input().split())
data = list(map(int, input().split()))
result = []

for i in range(0, n - k + 1):
    result.append(sum(data[i:i+k]))
    
print(max(result))