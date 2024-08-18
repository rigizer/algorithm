n = int(input())
result = ''
t = 0
while 9 ** t <= n:
    t += 1
result = ''
for i in range(t - 1, -1, -1):
    result += str(n // (9 ** i))
    n = n % (9 ** i)
print(result)