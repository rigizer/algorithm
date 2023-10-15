for _ in range(int(input())):
    nums = [*input().split()]
    cnt = 0
    for num in nums :
        if len(num) >= 2 :
            cnt += 1
    print(*nums)
    print(['zilch\n', 'double\n', 'double-double\n', 'triple-double\n'][cnt])