n = int(input())
arr = list(float(input()) for _ in range(n))
for i in range(1, n):
    arr[i] = max(arr[i], arr[i] * arr[i - 1])
print('%0.3f' % max(arr))