s = int(input())
f = sum(map(int, input().split()))

if s <= 240:
    print('high speed rail')
else:
    print('high speed rail' if s <= f else 'flight')