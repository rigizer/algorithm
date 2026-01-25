import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

candidate = None
count = 0
animals = []

for _ in range(n):
    species = input()
    animals.append(species)

    if count == 0:
        candidate = species
        count = 1
    elif species == candidate:
        count += 1
    else:
        count -= 1

if candidate is not None:
    occur = 0
    for species in animals:
        if species == candidate:
            occur += 1

    if occur * 2 > n:
        print(candidate)
    else:
        print('NONE')
else:
    print('NONE')