cnt = 0
for n in range(1, int(input()) + 1):
    for i in str(n):
        if i == '3' or i == '6' or i == '9':
            cnt += 1
print(cnt)