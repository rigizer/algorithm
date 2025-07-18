mod = 10 ** 9 + 7
inv2 = (mod + 1) // 2
n = int(input())
result = (pow(26, n, mod) + pow(22, n, mod)) % mod
result = result * inv2 % mod
print(result)