def s():
    n, k = map(int, input().split())
    sum_min = k * (k + 1) // 2
    if sum_min > n:
        return -1
    
    if (n - sum_min) % k == 0:
        return k - 1
    else:
        return k

print(s())