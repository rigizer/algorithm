def f(x: str) -> str:
    first_digit = int(x[0])
    num_digits = len(x)
    return str(first_digit * num_digits)

def isfa(x: str) -> str:
    seen = set()
    while x not in seen:
        seen.add(x)
        x = f(x)
    return 'FA'

x = input()
print(isfa(x))