import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
transactions = [int(input()) for _ in range(n)]

balance = 0
min_balance = 0

for t in transactions:
    balance += t
    if balance < min_balance:
        min_balance = balance

result = -min_balance if min_balance < 0 else 0
print(result)