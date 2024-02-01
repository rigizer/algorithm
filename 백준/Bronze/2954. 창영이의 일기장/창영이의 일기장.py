s = input()
i = 0
v = ['a', 'e', 'i', 'o', 'u']
while i < len(s):
    print(s[i], end='')
    if s[i] in v:
        i += 2
    i += 1