while True:
    a, b, c = map(int, input().split())
    # 0 0 0 입력 받으면 종료
    if (a, b, c) == (0, 0, 0):
        break

    # 등차수열
    if b - a == c - b:
        print('AP', c + (b - a))
        continue

    # 등비수열
    if b // a == c // b :
        print('GP', c * (b // a))
        continue