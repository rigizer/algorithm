while True:
    n = int(input())
    if n == 0:
        break
    num = 1
    for i in range(2, 2 * n, 2):
        num += i
    print(f'{n} => {num}')