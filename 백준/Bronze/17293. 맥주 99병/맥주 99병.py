n = int(input())
for i in range(n, 0, -1):
    if i == 1:
        print(f'1 bottle of beer on the wall, 1 bottle of beer.')
    else:
        print(f'{i} bottles of beer on the wall, {i} bottles of beer.')
    
    if i - 1 == 0:
        print('Take one down and pass it around, no more bottles of beer on the wall.')
    elif i - 1 == 1:
        print('Take one down and pass it around, 1 bottle of beer on the wall.')
    else:
        print(f'Take one down and pass it around, {i - 1} bottles of beer on the wall.')
    
    print()

print('No more bottles of beer on the wall, no more bottles of beer.')
if n == 1:
    print('Go to the store and buy some more, 1 bottle of beer on the wall.')
else:
    print(f'Go to the store and buy some more, {n} bottles of beer on the wall.')