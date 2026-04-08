import sys
input = lambda: sys.stdin.readline().rstrip()

s = input()
target = 'SciComLove'

result = 0

for i in range(10):
    if s[i] != target[i]:
        result += 1

print(result)