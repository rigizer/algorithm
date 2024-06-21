n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((b, a))
arr.sort(reverse=True)
ans = arr[0][0] - arr[0][1]
for i in range(1, n):
    if ans > arr[i][0]:
        ans = arr[i][0] - arr[i][1]
    else:
        ans -= arr[i][1]
print(ans if ans >= 0 else -1)