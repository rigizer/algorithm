def check(i, j):
	cnt = 0
	for a in range(5):
		for b in range(7):
			if n_list[i][a][b] != n_list[j][a][b]:
				cnt += 1
	return cnt

n = int(input())
n_list = []
for i in range(n):
	i_list= []
	for j in range(5):
		i_list.append(list(input()))
	n_list.append(i_list)	

min_n = 36
for i in range(n):
	for j in range(i + 1, n):
		num = check(i, j)
		if num < min_n:
			a, b = i, j
			min_n = num

print(a + 1, b + 1)