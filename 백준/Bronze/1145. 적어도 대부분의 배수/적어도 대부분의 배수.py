arr = list(map(int, input().split()))
min_num = min(arr)
cnt = 0
while True:
    cnt = 0
    for i in range(len(arr)):
        if min_num % arr[i] == 0 :
            cnt += 1
    if cnt >= 3:
        print(min_num)
        break
    min_num += 1