n, k, b = map(int, input().split())

traffic = [0] * (n + 1)
broken = [int(input()) for _ in range(b)]

for i in broken:
    traffic[i - 1] = 1

min_repairs = sum(traffic[:k])
cnt = min_repairs

for i in range(1, n - k + 1):
    if traffic[i - 1] == 1:
        cnt -= 1
    if traffic[i + k - 1] == 1:
        cnt += 1
    min_repairs = min(min_repairs, cnt)

print(min_repairs)