n, l = map(int, input().split())
pos = 0
answer = 0

for _ in range(n):
    d, r, g = map(int, input().split())

    answer += (d - pos)
    pos = d
    if answer % (r + g) <= r:
        answer += (r - (answer % (r + g)))

answer += (l - pos)
print(answer)