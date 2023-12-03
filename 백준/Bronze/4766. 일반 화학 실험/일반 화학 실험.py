data = []
while True:
    n = float(input())
    if n == 999:
        break
    data.append(n)

for i in range(1, len(data)):
    print('%.2f' % (data[i] - data[i - 1]))