import sys
input = lambda: sys.stdin.readline().rstrip()

n, m, b = map(int, input().split())

counts = [0] * 257
for _ in range(n):
    for x in map(int, input().split()):
        counts[x] += 1

best_time = 10**30
best_height = 0

for h in range(257):
    remove_blocks = 0
    add_blocks = 0

    for height in range(257):
        cnt = counts[height]
        if cnt == 0:
            continue

        if height > h:
            remove_blocks += (height - h) * cnt
        elif height < h:
            add_blocks += (h - height) * cnt

    if b + remove_blocks < add_blocks:
        continue

    time = remove_blocks * 2 + add_blocks

    if time < best_time or (time == best_time and h > best_height):
        best_time = time
        best_height = h

print(best_time, best_height)