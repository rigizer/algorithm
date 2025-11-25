import sys
input = lambda: sys.stdin.readline().rstrip()

def is_subsequence(m, w):
    i = 0
    for ch in w:
        if i < len(m) and m[i] == ch:
            i += 1
    return i == len(m)

m = input()
n = int(input())

best_word = None
best_ratio = -1

for _ in range(n):
    w, g = input().split()
    g = int(g)

    if not is_subsequence(m, w):
        continue

    added = len(w) - len(m)
    if added == 0:
        continue

    ratio = g / added

    if ratio > best_ratio:
        best_ratio = ratio
        best_word = w

if best_word is None:
    print('No Jam')
else:
    print(best_word)