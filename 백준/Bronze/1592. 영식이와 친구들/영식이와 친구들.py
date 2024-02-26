n, m, l = map(int, input().split())
data = [0] * n
c = i = 0
while data[i] < m - 1:
    data[i] += 1
    c += 1
    i = (i + l) % n if data[i] % 2 == 1 else (i - l) % n
print(c)