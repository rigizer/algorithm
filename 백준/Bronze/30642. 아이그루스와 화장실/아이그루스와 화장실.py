import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
animal = input()
k = int(input())

if animal == 'annyong':
    target = 1
else:
    target = 0

if k % 2 == target:
    result = k
else:
    lower = k - 1
    if lower >= 1 and lower % 2 == target:
        result = lower
    else:
        result = k + 1

print(result)