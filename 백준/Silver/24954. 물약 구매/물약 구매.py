import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
c = list(map(int, input().split()))

discount = [[] for _ in range(n)]
for i in range(n):
    p = int(input())
    for _ in range(p):
        a, d = map(int, input().split())
        discount[i].append((a - 1, d))

result = float('inf')

def dfs(bought_mask, current_costs, total):
    global result

    if total >= result:
        return

    if bought_mask == (1 << n) - 1:
        result = min(result, total)
        return

    for i in range(n):
        if not (bought_mask & (1 << i)):
            price = max(1, current_costs[i])

            new_costs = current_costs[:]
            for a, d in discount[i]:
                new_costs[a] -= d

            dfs(bought_mask | (1 << i), new_costs, total + price)

dfs(0, c[:], 0)

print(result)