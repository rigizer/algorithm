import sys
input = lambda: sys.stdin.readline().rstrip()

def make_even(candies, n):
    for i in range(n):
        if candies[i] % 2 == 1:
            candies[i] += 1

def all_equal(candies):
    return all(c == candies[0] for c in candies)

t = int(input())
for _ in range(t):
    n = int(input())
    candies = list(map(int, input().split()))

    make_even(candies, n)
    if all_equal(candies):
        print(0)
        continue

    count = 0
    while True:
        next_candies = [0] * n
        for i in range(n):
            give = candies[i] // 2
            next_candies[i] -= give
            next_candies[(i + 1) % n] += give

        for i in range(n):
            candies[i] += next_candies[i]
        make_even(candies, n)

        count += 1
        if all_equal(candies):
            print(count)
            break