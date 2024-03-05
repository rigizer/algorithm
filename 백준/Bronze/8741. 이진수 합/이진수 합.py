k = int(input())
t = 2 ** k - 1
r = t * (t + 1) // 2
print(bin(r)[2:])