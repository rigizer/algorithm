tc = int(input())
for _ in range(tc):
    t = int(input())
    data = list(map(int, input().split()))
    
    d = {}
    for x in data:
        d[x] = d.get(x, 0) + 1
    r = sorted(d.items(), key=lambda x: (-x[1], -x[0]))
    print(f'#{t} {r[0][0]}')