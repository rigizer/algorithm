import sys
input = lambda: sys.stdin.readline().rstrip()

s = input()
order = ['H', 'O', 'N', 'I']

idx = 0
result = 0

for ch in s:
    if ch == order[idx]:
        idx += 1
        if idx == 4:
            result += 1
            idx = 0

print(result)