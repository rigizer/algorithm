x = []
for i in range(10):
    x.append(int(input()))
print(int(sum(x) / 10))
y = list(set(x))
z = []
for i in range(len(y)):
    z.append(x.count(y[i]))
print(y[z.index(max(z))])