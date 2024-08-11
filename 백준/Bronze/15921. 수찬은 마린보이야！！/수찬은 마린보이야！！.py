n = int(input())
if n == 0:
    print('divide by zero')
else:
    li = list(map(int, input().split()))
    ans = sum(li)/n / (sum(li)/n)
    print('%.2f' % ans)