for _ in range(int(input())):
    n = int(input())
    store = sorted(map(int, input().split()))
    print((store[-1] - store[0]) * 2)