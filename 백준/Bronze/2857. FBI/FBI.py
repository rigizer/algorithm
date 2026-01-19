import sys
input = lambda: sys.stdin.readline().rstrip()

agents = [input() for _ in range(5)]
result = []

for i, v in enumerate(agents):
    if 'FBI' in v:
        result.append(i + 1)

if result == []:
    print('HE GOT AWAY!')
else:
    print(*result)