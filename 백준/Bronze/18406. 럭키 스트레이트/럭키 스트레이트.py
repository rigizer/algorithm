n = input()
data = list(map(int, n))
length = len(data)

if sum(data[:(length//2)]) == sum(data[(length//2):]):
    print('LUCKY')
else:
    print('READY')