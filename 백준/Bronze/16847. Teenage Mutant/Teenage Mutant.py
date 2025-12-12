import sys
input = lambda: sys.stdin.readline().rstrip()

K = int(input())
for t in range(1, K + 1):
    n, k = map(int, input().split())
    me = input()
    ancestors = [input() for _ in range(n)]

    mutant = 0
    for col in range(k):
        my_char = me[col]
        ok = True
        for anc in ancestors:
            if anc[col] == my_char:
                ok = False
                break
        if ok:
            mutant += 1

    print(f'Data Set {t}:')
    print(f'{mutant}/{k}')
    print()