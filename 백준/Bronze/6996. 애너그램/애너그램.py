import sys
input = lambda: sys.stdin.readline().rstrip()

result = []
t = int(input())
for _ in range(t):
    a, b = input().split()
    if sorted(a) == sorted(b):
        result.append(f'{a} & {b} are anagrams.')
    else:
        result.append(f'{a} & {b} are NOT anagrams.')
print('\n'.join(result))