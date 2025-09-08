import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
result = []

for _ in range(t):
    m = int(input())
    people = 0
    min_people = 0
    for _ in range(m):
        p1, p2 = map(int, input().split())
        people += p1
        people -= p2
        if people < 0:
            min_people += -people
            people = 0
    result.append(str(min_people))

print('\n'.join(result))