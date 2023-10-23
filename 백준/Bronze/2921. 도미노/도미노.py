n = int(input())
r = 0
for i in range(1, n + 1):
    r += 1.5 * i * (i + 1)
print(int(r))