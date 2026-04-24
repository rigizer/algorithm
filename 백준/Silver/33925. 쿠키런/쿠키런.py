import sys

input_data = sys.stdin.read().split()
if not input_data:
    sys.exit()

n, j_limit, s_limit, h, k = map(int, input_data[:5])
r0, r1, r2 = input_data[5], input_data[6], input_data[7]

dp = [[-1] * (s_limit + 1) for _ in range(j_limit + 1)]
dp[0][0] = h

for i in range(1, n):
    nxt = [[-1] * (s_limit + 1) for _ in range(j_limit + 1)]
    obs = 0
    if r0[i] == 'v':
        obs = 3
    elif r1[i] == '^':
        obs = 2
    elif r2[i] == '^':
        obs = 1
    
    for j in range(j_limit + 1):
        for s in range(s_limit + 1):
            hp = dp[j][s]
            if hp <= 0:
                continue
            
            if obs == 0:
                if hp > nxt[j][s]:
                    nxt[j][s] = hp
            else:
                if hp - k > 0:
                    if hp - k > nxt[j][s]:
                        nxt[j][s] = hp - k
                
                if obs == 1:
                    if j + 1 <= j_limit:
                        if hp > nxt[j+1][s]:
                            nxt[j+1][s] = hp
                elif obs == 2:
                    if j + 2 <= j_limit:
                        if hp > nxt[j+2][s]:
                            nxt[j+2][s] = hp
                elif obs == 3:
                    if s + 1 <= s_limit:
                        if hp > nxt[j][s+1]:
                            nxt[j][s+1] = hp
    dp = nxt

ans = -1
for row in dp:
    for val in row:
        if val > ans:
            ans = val

print(ans)