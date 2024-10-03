n = int(input())
for i in range(n):
    tmp = [0, 0]
    while True:
        s = input()
        if s == '':
            break
        else:
            tmp[0] += len(s)
            tmp[1] += len(s) - s.count('#')
    sum = round(100 * tmp[1] / tmp[0], 1)
    
    if sum % 1 == 0:
        print('Efficiency ratio is %d%%.' % int(sum))
    else:
        print('Efficiency ratio is %.1f%%.' % sum)