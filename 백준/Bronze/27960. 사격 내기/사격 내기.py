a, b = map(int, input().split())
bin_a, bin_b = bin(a), bin(b)

result = int(bin(a^b)[2:], 2)
print(result)