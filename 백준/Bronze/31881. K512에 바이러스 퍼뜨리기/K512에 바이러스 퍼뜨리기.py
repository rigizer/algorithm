import sys
input = sys.stdin.readline

n, q = map(int, input().split())
virus_computer = [False] * (n + 1)
result = n

for _ in range(q):
    query = input().split()
    if len(query) > 1:
        case, x = int(query[0]), int(query[1])
    else:
        case = int(query[0])
    if case == 1:
        if not virus_computer[x]:
            result -= 1
        virus_computer[x] = True
    elif case == 2:
        if virus_computer[x]:
            result += 1
        virus_computer[x] = False
    elif case == 3:
        print(result)