n = int(input())
cost = []

for _ in range(n):
    price = list(map(int, input().split()))
    cost.append([price[0], price[1]])

cost.sort(key = lambda x: (x[0], x[1]))

total = [0] * n

for i in range(n):
    for j in range(i, n):
        benefit = cost[i][0] - cost[j][1]
        if benefit > 0:
            total[i] += benefit
result = [cost[i][0] for i in range(n) if total[i] == max(total)]

print(0 if sum(total) == 0 else min(result))