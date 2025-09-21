import sys
from itertools import permutations
input = lambda: sys.stdin.readline().rstrip()

def solution(arr):
    for x, y, z in permutations(arr, 3):
        if (x - y) / z != (x - y) // z:
            return 'no'
    return 'yes'

n = int(input())
arr = list(map(int, input().split()))
result = solution(arr)
print(result)