r, c = map(int, input().split())
a, b = map(int, input().split())

li = []
t1, t2 = '', ''
for i in range(c):
    t1 += '.' * b if i % 2 else 'X' * b
    t2 += 'X' * b if i % 2 else '.' * b
    
for i in range(r):
    for _ in range(a):
        print(t2 if i % 2 else t1)