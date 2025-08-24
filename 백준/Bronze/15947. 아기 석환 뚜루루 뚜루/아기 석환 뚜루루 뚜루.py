n = int(input())

idx = (n - 1) % 14
r = (n - 1) // 14

if idx == 0 or idx == 12:
    result = 'baby'
elif idx == 1 or idx == 13:
    result = 'sukhwan'
elif idx == 4:
    result = 'very'
elif idx == 5:
    result = 'cute'
elif idx == 8:
    result = 'in'
elif idx == 9:
    result = 'bed'
else:
    if idx == 2 or idx == 6 or idx == 10:
        k = 2 + r
    else:
        k = 1 + r
    if k >= 5:
        result = f'tu+ru*{k}'
    else:
        result = 'tu' + 'ru' * k

print(result)