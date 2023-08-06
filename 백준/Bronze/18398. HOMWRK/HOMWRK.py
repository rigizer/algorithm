for _ in range(int(input())):
    p = int(input())
    for j in range(p):
        n = list(map(int, input().split()))
        print(n[0] + n[1], n[0] * n[1])