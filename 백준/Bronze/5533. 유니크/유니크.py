n = int(input())
data = [[],[],[]]
score = [0] * n
for i in range(n):
    t = list(map(int,input().split()))
    data[0].append(t[0])
    data[1].append(t[1])
    data[2].append(t[2])
for i in range(3):
    for j in range(n):
        if data[i].count(data[i][j]) > 1:
            score[j] += 0
        else:
            score[j] += data[i][j]
for i in score:
    print(i)