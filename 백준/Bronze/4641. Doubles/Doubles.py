while True:
    ns = list(map(int, input().split()))
    if ns[0] == -1: break

    result = 0
    size = len(ns)
    for i in range(size - 1):
        for j in range(i, size - 1):
            if ns[i] == ns[j] * 2 or ns[j] == ns[i] * 2:
                result += 1
    
    print(result)