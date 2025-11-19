tc = int(input())
for t in range(1, tc + 1):
    s = input()
    yyyy = s[0:4]
    mm = s[4:6]
    dd = s[6:8]
    
    if 1 <= int(mm) < 12:
        if int(mm) in [1, 3, 5, 7, 8, 10, 12] and 1 <= int(dd) <= 31:
            print(f'#{t} {yyyy}/{mm}/{dd}')
        elif int(mm) in [4, 6, 9, 11] and 1 <= int(dd) <= 30:
            print(f'#{t} {yyyy}/{mm}/{dd}')
        elif int(mm) == 2 and 1 <= int(dd) <= 28:
            print(f'#{t} {yyyy}/{mm}/{dd}')
        else:
            print(f'#{t} -1')
    else:
        print(f'#{t} -1')