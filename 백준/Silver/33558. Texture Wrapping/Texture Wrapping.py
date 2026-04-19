import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
u, v = map(int, input().split())
tex = [input() for _ in range(u)]
mode = input()

result = []

if mode == 'clamp-to-edge':
    for i in range(n):
        ti = i if i < u else u - 1
        row = []
        for j in range(m):
            tj = j if j < v else v - 1
            row.append(tex[ti][tj])
        result.append(''.join(row))

elif mode == 'repeat':
    for i in range(n):
        ti = i % u
        row = []
        for j in range(m):
            tj = j % v
            row.append(tex[ti][tj])
        result.append(''.join(row))

else:  # mirrored-repeat
    for i in range(n):
        ti = i % (2 * u)
        if ti >= u:
            ti = 2 * u - 1 - ti
        row = []
        for j in range(m):
            tj = j % (2 * v)
            if tj >= v:
                tj = 2 * v - 1 - tj
            row.append(tex[ti][tj])
        result.append(''.join(row))

sys.stdout.write('\n'.join(result))