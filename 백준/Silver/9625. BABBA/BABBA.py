n = int(input())
a, b = [1], [0]

for i in range(n):
    a.append(b[i])
    b.append(b[i] + a[i])

print(a[-1], end = ' ')
print(b[-1])