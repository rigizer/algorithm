def calc(h, w, block):
    result = 0

    for i in range(1, h + 1):
        chk = 0
        start = False

        for j in range(w):
            if start == False:
                if block[j] >= i:
                    start = True
            elif start == True:
                if block[j] < i:
                    chk += 1
                else:
                    if chk == 0:
                        continue

                    result += chk
                    chk = 0
                    start = True

    return result

h, w = map(int, input().split())
block = list(map(int, input().split()))

result = calc(h, w, block)
print(result)