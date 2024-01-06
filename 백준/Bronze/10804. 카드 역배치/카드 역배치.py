data = [i for i in range(1, 21)]
for i in range(10):
    m, n = map(int, input().split())
    a = data[:m - 1]
    b = data[m - 1:n][::-1]
    c = data[n:]
    data = a + b + c
    
for i in data:
    print(i, end=' ')