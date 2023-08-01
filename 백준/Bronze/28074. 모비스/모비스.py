data = input()
for c in 'MOBIS':
    if c not in data:
        print('NO')
        break
else:
    print('YES')