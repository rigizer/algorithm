n, m = map(int, input().split())
m = (m // 2) + 1
p_cnt = 0
for i in range(n) : 
    r = input()
    cnt = 0
    for j in r : 
        if j == 'O' : 
            cnt += 1
    
    if m <= cnt : 
        p_cnt += 1
        
print(p_cnt)