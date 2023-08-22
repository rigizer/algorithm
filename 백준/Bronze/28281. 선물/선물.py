n, x = map(int, input().split())
socks = list(map(int, input().split()))
price = []

for i in range(n - 1):
    price.append((socks[i] + socks[i + 1]) * x)

print(min(price))