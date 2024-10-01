while True:
    n = input()
    if n == "0":
        break
    while True:
        if len(n) == 1:
            print(n)
            break
        n = str(sum(list(map(int, list(n)))))