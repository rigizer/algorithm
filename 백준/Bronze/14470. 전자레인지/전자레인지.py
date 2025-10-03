li = [int(input()) for _ in range(5)]
if li[0] <= 0:
    print(-li[0]*li[2] + li[3] + li[1]*li[4])
else:
    print((li[1]-li[0])*li[4])