c = int(input())
m = 0
for i in range(c):
    s = input()
    cnt = 0
    for j in range(len(s)):
        if((j+2 < len(s)) and (s[j] == 'f' and s[j+1] == 'o' and s[j+2] == 'r')):
            cnt += 1
            j = j+2
        elif((j+4 < len(s)) and (s[j] == 'w' and s[j+1] == 'h' and s[j+2] == 'i' and s[j+3] == 'l' and s[j+4] == 'e')):
            cnt += 1
            j = j+4
    m = max(m,cnt)

print(m)