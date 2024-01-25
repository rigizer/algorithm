N = int(input())
trophy = [int(input()) for _ in range(N)]

max_left, max_right = trophy[0], trophy[-1]
left, right = 1, 1

for i in range(1, N) :
    if max_left < trophy[i] :
        left += 1
        max_left = trophy[i]
    else :
        continue

for j in range(N-1, -1, -1) :
    if max_right < trophy[j] :
        right += 1
        max_right = trophy[j]
    else :
        continue

print(left)
print(right)
