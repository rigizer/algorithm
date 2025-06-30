k = int(input())
sieve = [True] * (8_000_001)
sieve[0] = sieve[1] = False
count = 0
for i in range(2, 8_000_001):
    if sieve[i]:
        count += 1
        if count == k:
            print(i)
            break
        for j in range(i * i, 8_000_001, i):
            sieve[j] = False