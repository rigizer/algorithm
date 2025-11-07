import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    n = int(input())
    applicants = []
    for _ in range(n):
        a, b = map(int, input().split())
        applicants.append((a, b))

    applicants.sort(key=lambda x: x[0])

    result = 1
    best_interview = applicants[0][1]

    for i in range(1, n):
        if applicants[i][1] < best_interview:
            result += 1
            best_interview = applicants[i][1]

    print(result, end='')
    if _ != t - 1:
        print()