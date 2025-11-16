import sys
input = lambda: sys.stdin.readline().rstrip()

w1, w2 = input().split()
length = min(len(w1), len(w2))
result = []

for i in range(length):
    if i % 2 == 0:
        result.append(w1[i])
    else:
        result.append(w2[i])

print(''.join(result))