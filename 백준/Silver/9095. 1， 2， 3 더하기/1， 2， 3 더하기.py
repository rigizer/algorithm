result = 0

def func(x, n):
    global result

    if x == n:
        result += 1
        return
    elif x > n:
        return

    for i in range(1, 4):
        func(x + i, n)

for _ in range(int(input())):
    result = 0
    n = int(input())
    func(0, n)
    print(result)