def calc(n):
    str_n = str(n)
    s = sum(int(i) for i in str_n)
    s = 9 - (s % 9)
    if s == 9:
        s = 0

    result = set()
    for i in range(len(str_n) + 1):
        if s == 0 and i == 0:
            continue
        x = str_n[:i]
        y = str_n[i:]

        if i == len(str_n) or s < int(str_n[i]):
            return int(x + str(s) + y)

for tc in range(int(input())):
    n = int(input())
    result = calc(n)
    print(f'Case #{tc + 1}: {result}')