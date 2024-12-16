import sys

input = sys.stdin.readline
n = int(input())
data = []

for i in range(n):
    x = int(input())
    data.append(x)

data = sorted(data, reverse=False)
for i in range(n):
    print(data[i])