for _ in range(int(input())):
    n = int(input())
    ns = [int(input()) for i in range(n)]
    result = 0
    
    while True:
        result += 1
        if len({i % result for i in ns}) == n:
            print(result)
            break