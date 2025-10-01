s = input().strip()

result = 0
cur = 0
prev = ''

for ch in s:
    if prev != '' and ch > prev:
        cur += 1
    else:
        cur = 1

    result += cur
    prev = ch

print(result)