import sys

x = int(sys.stdin.readline())
min_calc = sys.maxsize

def dp(n, calc):
    global min_calc

    if calc > min_calc:
        return

    if n == 1:
        min_calc = min(min_calc, calc)
        return
    elif n < 1:
        return

    if n % 3 == 0:
        dp(n // 3, calc + 1)
    if n % 2 == 0:
        dp(n // 2, calc + 1)
    dp(n - 1, calc + 1)

dp(x, 0)
print(min_calc)