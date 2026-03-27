import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
dictionary = set()

for _ in range(n):
    dictionary.add(input())

m = int(input())

for i in range(1, m + 1):
    unknown = []

    while True:
        word = input()
        if word == '-1':
            break

        if word not in dictionary:
            unknown.append(word)

    if not unknown:
        print(f'Email {i} is spelled correctly.')
    else:
        print(f'Email {i} is not spelled correctly.')
        for w in unknown:
            print(w)

print('End of Output')