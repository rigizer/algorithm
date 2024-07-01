s1, s2 = map(str, input().split())

ans = ''
if len(s1) < len(s2):
    s1 = s1.zfill(len(s2))
else:
    s2 = s2.zfill(len(s1))
for i in range(len(s1)):
    ans += str(int(s1[i]) + int(s2[i]))

print(ans)