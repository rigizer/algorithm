n = int(input())
arr = []
result = []
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
         
for i in range(n):
    result.append(arr[i] * (i + 1))
print(max(result))