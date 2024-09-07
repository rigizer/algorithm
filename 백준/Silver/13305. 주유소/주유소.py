n = int(input())
distance = list(map(int, input().split()))
oil_cost = list(map(int, input().split()))
 
total = distance[0] * oil_cost[0]
min_cost = oil_cost[0]
 
for i in range(1, n - 1):
    if min_cost > oil_cost[i]: 
        min_cost = oil_cost[i]
    total += min_cost * distance[i]

print(total)