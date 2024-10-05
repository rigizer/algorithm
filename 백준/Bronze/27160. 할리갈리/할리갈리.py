d = {}
for _ in range(int(input())):
    s, x = input().split()
    d[s] = d.get(s, 0) + int(x)

for n in d:
    if d[n] == 5:
        print('YES')
        exit()

print('NO')