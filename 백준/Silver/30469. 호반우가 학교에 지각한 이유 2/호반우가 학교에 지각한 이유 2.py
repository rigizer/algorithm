import sys

sys.setrecursionlimit(2000)

input_data = sys.stdin.read().split()
if input_data:
    a = int(input_data[0])
    b = int(input_data[1])
    n = int(input_data[2])

    primes = set()
    for i in range(10, 100):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.add(i)

    str_b = str(b)
    memo = set()

    def dfs(idx, current_val):
        if idx == n:
            if current_val[-2:] == str_b:
                return current_val
            return None

        last_digit = int(current_val[-1])
        state = (idx, last_digit)

        if state in memo:
            return None

        for nxt in range(10):
            if (last_digit * 10 + nxt) in primes:
                res = dfs(idx + 1, current_val + str(nxt))
                if res:
                    return res

        memo.add(state)
        return None

    ans = dfs(2, str(a))
    if ans:
        print(ans)
    else:
        print('-1')