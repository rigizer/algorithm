n = int(input())
a = list(map(int, input().split()))
min_avg = float('inf')
min_index = -1

for i in range(n - 1):
    avg2 = (a[i] + a[i + 1]) / 2
    if avg2 < min_avg:
        min_avg = avg2
        min_index = i

    if i + 2 < n:
        avg3 = (a[i] + a[i + 1] + a[i + 2]) / 3
        if avg3 < min_avg:
            min_avg = avg3
            min_index = i

print(min_index)