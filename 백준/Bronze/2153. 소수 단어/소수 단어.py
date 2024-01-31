import math

word = input()
total = 0
for w in word:
    if w.islower():
        total += ord(w) - 96
    else:
        total += ord(w) - 38

is_prime = True
for i in range(2, int(math.sqrt(total)) + 1):
    if total % i == 0:
        is_prime = False

print('It is a prime word.' if is_prime else 'It is not a prime word.')