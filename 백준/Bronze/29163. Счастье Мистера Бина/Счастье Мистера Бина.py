n = int(input())
ns = list(map(int, input().split()))

odd = 0
even = 0
for i in ns:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

if odd < even:
    print('Happy')
else:
    print('Sad')