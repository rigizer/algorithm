import sys

data = sys.stdin.readlines()
numbers = []
for i in data:
    for j in i.split():
        numbers.append(int(j[::-1]))
numbers = numbers[1:]
numbers.sort()
print('\n'.join(map(str, numbers)))