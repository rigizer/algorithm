import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))
ops = list(map(int, input().split()))  # +, -, *, /

max_value = -10**18
min_value = 10**18

def div_cpp(a, b):
    if a < 0:
        return -((-a) // b)
    return a // b

def dfs(idx, value, add, sub, mul, div):
    global max_value, min_value

    if idx == N:
        if value > max_value:
            max_value = value
        if value < min_value:
            min_value = value
        return

    x = A[idx]

    if add > 0:
        dfs(idx + 1, value + x, add - 1, sub, mul, div)
    if sub > 0:
        dfs(idx + 1, value - x, add, sub - 1, mul, div)
    if mul > 0:
        dfs(idx + 1, value * x, add, sub, mul - 1, div)
    if div > 0:
        dfs(idx + 1, div_cpp(value, x), add, sub, mul, div - 1)

dfs(1, A[0], ops[0], ops[1], ops[2], ops[3])

print(max_value)
print(min_value)