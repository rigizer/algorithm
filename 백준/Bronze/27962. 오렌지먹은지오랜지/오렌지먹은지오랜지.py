n = int(input())
s = input()
answer = 'NO'
for i in range(1, n):
    a = s[:i]
    b = s[n-i:]
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[j]:
            cnt+=1
    if cnt == 1:
        answer = 'YES'
        break
print(answer)