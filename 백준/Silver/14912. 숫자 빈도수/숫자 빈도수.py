n, num = map(int,input().split())
cnt = 0
for i in range(1, n + 1):
	for a in str(i):
		if int(a) == num:
			cnt += 1
print(cnt)