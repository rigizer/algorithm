for _ in range(int(input())):
    s = 0
    m = 1e9
    for i in list(map(int, input().split())):
        if i % 2 == 0:
            s += i
            m = min(m, i)
    
    print(s, m)