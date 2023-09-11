t = int(input())
for x in range(1, t + 1):
    n = int(input())
    if n <= 25:
        print(f'Case #{x}: World Finals')
    elif n <= 1000:
        print(f'Case #{x}: Round 3')
    elif n <= 4500:
        print(f'Case #{x}: Round 2')
    else:
        print(f'Case #{x}: Round 1')