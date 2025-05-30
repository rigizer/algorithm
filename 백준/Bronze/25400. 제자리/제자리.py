n = int(input())
arr = list(map(int, input().split()))

start = 1
cnt = 0
for a in arr:
    if a == start:
        start += 1
    else:
        cnt += 1

print(cnt)