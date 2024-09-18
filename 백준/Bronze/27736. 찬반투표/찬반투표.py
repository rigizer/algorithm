n = int(input())
n_list = list(map(int, input().split()))
approved, rejected, invalid = 0, 0, 0

for i in n_list:
    if i == 1:
        approved += 1
    elif i == -1:
        rejected += 1
    else:
        invalid += 1

if invalid >= n / 2:
    print('INVALID')
elif approved > rejected:
    print('APPROVED')
else:
    print('REJECTED')