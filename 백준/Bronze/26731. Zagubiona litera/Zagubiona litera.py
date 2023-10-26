import string

s = input()
for a in string.ascii_uppercase :
    if a not in s :
        print(a)
        break