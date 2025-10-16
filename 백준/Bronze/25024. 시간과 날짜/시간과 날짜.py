import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())

month_days = {
    1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

for _ in range(t):
    x, y = map(int, input().split())

    if 0 <= x <= 23 and 0 <= y <= 59:
        time_valid = 'Yes'
    else:
        time_valid = 'No'

    if 1 <= x <= 12 and 1 <= y <= month_days[x]:
        date_valid = 'Yes'
    else:
        date_valid = 'No'

    print(time_valid, date_valid, end='')
    if _ != t - 1:
        print()