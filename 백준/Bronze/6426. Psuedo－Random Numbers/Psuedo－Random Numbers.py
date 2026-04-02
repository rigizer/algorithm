import sys
input = lambda: sys.stdin.readline().rstrip()

case = 1

while True:
    z, i, m, l = map(int, input().split())
    if z == 0 and i == 0 and m == 0 and l == 0:
        break

    visited = [-1] * m
    count = 0

    while visited[l] == -1:
        visited[l] = count
        count += 1
        l = (z * l + i) % m

    cycle_length = count - visited[l]

    print(f'Case {case}: {cycle_length}')
    case += 1