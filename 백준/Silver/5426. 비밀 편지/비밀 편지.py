for _ in range(int(input())):
    msg = input()
    n = int(len(msg) ** (1 / 2))
    decoded_msg = ''
    for i in range(n, 0, -1):
        for j in range(i, n * n + 1, n):
            decoded_msg += msg[j - 1]
    print(decoded_msg)