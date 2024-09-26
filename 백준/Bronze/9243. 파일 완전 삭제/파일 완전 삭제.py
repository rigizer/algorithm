n = int(input())
before = list(map(int, input()))
after = list(map(int, input()))
if n % 2:
    for i in range(len(before)):
        if before[i] == 0:
            before[i] = 1
        else:
            before[i] = 0
if before == after:
    print('Deletion succeeded')
else:
    print('Deletion failed')