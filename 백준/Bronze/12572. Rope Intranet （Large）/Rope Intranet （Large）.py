import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for case in range(1, t + 1):
    n = int(input())
    wires = []
    for _ in range(n):
        a, b = map(int, input().split())
        wires.append((a, b))
    wires.sort()
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if wires[i][1] > wires[j][1]:
                count += 1
    print(f'Case #{case}: {count}', end='')
    if case != t:
        print()