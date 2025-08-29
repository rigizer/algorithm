import sys
input = lambda: sys.stdin.readline().rstrip()

result = []
n = int(input())
t = list(map(int, input().split()))
t.sort()

index = (n - 1) // 2
m = n - index
if n % 2 == 0:
    m -= 1
result.append(t[index])

for i in range(1, m):
    result.append(t[index + i])
    result.append(t[index - i])
    
if n % 2 == 0:
    result.append(t[n - 1])

print(' '.join(map(str, result)))