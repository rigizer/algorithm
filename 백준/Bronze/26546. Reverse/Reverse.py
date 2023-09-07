for _ in range(int(input())):
    s, i, j = input().split()
    print(s[:int(i)] + s[int(j):])