for _ in range(3):
    s = str(input())
    mymax = 1
    cnt = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            mymax = max(cnt, mymax)
            cnt = 1
    mymax = max(cnt, mymax)
    print(mymax)