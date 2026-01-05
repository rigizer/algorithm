import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
out = []

for _ in range(t):
    n = int(input())
    robots = [input() for _ in range(n)]
    k = len(robots[0])
    alive = [True] * n

    for r in range(k):
        has_rock = False
        has_scissors = False
        has_paper = False

        for i in range(n):
            if not alive[i]:
                continue
            c = robots[i][r]
            if c == 'R':
                has_rock = True
            elif c == 'S':
                has_scissors = True
            else:
                has_paper = True

        loser = None
        if has_rock and has_scissors and not has_paper:
            loser = 'S'
        elif has_scissors and has_paper and not has_rock:
            loser = 'P'
        elif has_paper and has_rock and not has_scissors:
            loser = 'R'

        if loser:
            for i in range(n):
                if alive[i] and robots[i][r] == loser:
                    alive[i] = False

        remain = [i for i in range(n) if alive[i]]
        if len(remain) == 1:
            out.append(str(remain[0] + 1))
            break

        if r == k - 1:
            if len(remain) == 1:
                out.append(str(remain[0] + 1))
            else:
                out.append('0')

print('\n'.join(out))