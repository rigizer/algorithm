import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
data = []
for _ in range(n):
    name, score = input().split()
    score = int(score)
    data.append((name, score))

data.sort(key=lambda x: (-x[1], x[0]))
print(data[0][0])