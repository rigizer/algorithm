for _ in range(int(input())):
    h, m, s = map(lambda string: bin(int(string))[2:].rjust(6, '0'), input().split(':'))
    col = ''.join([a + b + c for a, b, c in zip(h, m, s)])
    row = h + m + s
    print(f'{col} {row}')