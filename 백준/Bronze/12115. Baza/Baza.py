import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
db = [list(map(int, input().split())) for _ in range(n)]
q = int(input())

for i in range(q):
    query = list(map(int, input().split()))
    result = 0

    for row in db:
        ok = True
        for j in range(m):
            if query[j] != -1 and query[j] != row[j]:
                ok = False
                break

        if ok:
            result += 1

    print(result)