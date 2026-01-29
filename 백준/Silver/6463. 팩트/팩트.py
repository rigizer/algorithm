import sys
input = lambda: sys.stdin.readline().rstrip()

def last_non_zero_digit(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        while result % 10 == 0:
            result //= 10
        result %= 100000
    return result % 10

nums = []
while True:
    line = input()
    if not line:
        break
    nums.append(int(line))

output = []
for n in nums:
    digit = last_non_zero_digit(n)
    output.append(f'{n:5d} -> {digit}')

print('\n'.join(output))