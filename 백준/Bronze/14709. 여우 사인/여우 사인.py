n = int(input())
pairs = set()

for _ in range(n):
    a, b = map(int, input().split())
    pair = tuple(sorted((a, b)))
    pairs.add(pair)

required = {(1, 3), (1, 4), (3, 4)}

if not required.issubset(pairs):
    print('Woof-meow-tweet-squeek')
    exit()

for a, b in pairs:
    if 2 in (a, b) or 5 in (a, b):
        print('Woof-meow-tweet-squeek')
        exit()

print('Wa-pa-pa-pa-pa-pa-pow!')