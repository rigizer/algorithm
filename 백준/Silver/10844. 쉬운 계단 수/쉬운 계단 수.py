import sys
input = lambda: sys.stdin.readline().rstrip()

MOD = 1000000000

N = int(input())

if N == 1:
    result = 9
    sys.stdout.write(str(result))
else:
    prev = [0] * 10
    for d in range(1, 10):
        prev[d] = 1

    for _ in range(2, N + 1):
        curr = [0] * 10
        curr[0] = prev[1] % MOD
        curr[9] = prev[8] % MOD
        for d in range(1, 9):
            curr[d] = (prev[d - 1] + prev[d + 1]) % MOD
        prev = curr

    result = sum(prev) % MOD
    sys.stdout.write(str(result))