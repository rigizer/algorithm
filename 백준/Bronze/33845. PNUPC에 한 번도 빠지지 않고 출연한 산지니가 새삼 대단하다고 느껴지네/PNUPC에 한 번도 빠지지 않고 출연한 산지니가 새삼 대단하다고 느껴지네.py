s, t = input(), input()
result = ''
for ch in t:
    if ch not in s:
        result += ch
print(result)