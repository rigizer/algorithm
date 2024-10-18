n, m = map(int, input().split())
j = int(input())
now = 1
apples = []
answer = 0
for _ in range(j):
    apples.append(int(input()))
for apple in apples:
    if now <= apple and now + (m - 1) >= apple:
        pass
    elif now > apple:
        answer += abs(apple - now)
        now = apple
    else:
        answer += apple - (m - 1) - now
        now = apple - (m - 1)
print(answer)