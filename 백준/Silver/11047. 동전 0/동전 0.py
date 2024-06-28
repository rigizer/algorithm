n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)

answer = 0
for coin in coins:
    if k >= coin:
        answer += k // coin
        k %= coin
        if k <= 0:
       		break
print(answer)