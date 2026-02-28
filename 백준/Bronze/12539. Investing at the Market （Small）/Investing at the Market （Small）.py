import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for tc in range(1, T + 1):
    M = int(input())
    prices = list(map(int, input().split()))
    
    max_profit = -1
    buy_month = -1
    sell_month = -1
    best_buy_price = float('inf')
    
    for B in range(11):
        buy_price = prices[B]
        count = M // buy_price
        
        if count == 0:
            continue
        
        for S in range(B + 1, 12):
            sell_price = prices[S]
            profit = count * (sell_price - buy_price)
            
            if profit > max_profit:
                max_profit = profit
                buy_month = B + 1
                sell_month = S + 1
                best_buy_price = buy_price
            
            elif profit == max_profit and profit > 0:
                if buy_price < best_buy_price:
                    buy_month = B + 1
                    sell_month = S + 1
                    best_buy_price = buy_price
    
    if max_profit <= 0:
        print(f'Case #{tc}: IMPOSSIBLE')
    
    else:
        print(f'Case #{tc}: {buy_month} {sell_month} {max_profit}')