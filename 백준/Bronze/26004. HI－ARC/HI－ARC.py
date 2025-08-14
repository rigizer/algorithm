n = int(input())
word = input()

h, i, a, r, c = 0, 0, 0, 0, 0

for ch in word:
    if ch == 'H':
        h += 1
    elif ch == 'I':
        i += 1
    elif ch == 'A':
        a += 1
    elif ch == 'R':
        r += 1
    elif ch == 'C':
        c += 1

print(min(h, i, a, r, c))