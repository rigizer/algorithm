import sys

data = sys.stdin.read().strip().split()
n = int(data[0])

result = [0] * (n + 1)
for k in range(1, n + 1):
    g = int(data[k])
    result[g] = k

sys.stdout.write('\n'.join(str(result[i]) for i in range(1, n + 1)) + '\n')