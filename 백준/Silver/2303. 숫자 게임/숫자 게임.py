n = int(input())
best_s = []
for i in range(n):
    cards = [*map(int, input().split())]
    max_n = 0
    for one in range(5):
        for two in range(one+1, 5):
            for three in range(two+1, 5):
                temp = (cards[one]+cards[two]+cards[three]) % 10
                if max_n < temp:
                    max_n = temp
    best_s.append(max_n)
best = max(best_s)
for i in range(n-1, -1, -1):
    if best == best_s[i]:
        print(i+1)
        break