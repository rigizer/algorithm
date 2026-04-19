import sys

input_data = sys.stdin.read().split()
if not input_data:
    sys.exit()

n, m = map(int, input_data[:2])
a = list(map(int, input_data[2:2+n]))
b = list(map(int, input_data[2+n:2+n+m]))

a.sort(reverse=True)
b.sort(reverse=True)

a_cnt = 1
b_cnt = 0

i = 0
j = 0

while True:
    moved = False

    if i < n and a_cnt > 0 and b_cnt == 0 and j < m:
        a_cnt -= 1
        b_cnt += a[i]
        i += 1
        moved = True

    if j < m and b_cnt > 0:
        b_cnt -= 1
        a_cnt += b[j]
        j += 1
        moved = True

    if not moved:
        break

print(a_cnt)