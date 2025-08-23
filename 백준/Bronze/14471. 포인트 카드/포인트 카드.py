n, m = map(int, input().split())
card_stamp = []
cnt = m - 1
for _ in range(m):
    a, b = map(int, input().split())
    if a < n:
        card_stamp.append(n - a)
    else:
        cnt -= 1

card_stamp.sort()
total_value = 0
if cnt > 0:
    for i in range(cnt):
        total_value += card_stamp[i]

print(total_value)