i = 1
while True:
    l, p, v = map(int, input().split())
    if (l, p, v) == (0, 0, 0):
        break
        
    camping = (l * (v // p)) + min((v % p), l)
    print('Case {}:'.format(i), camping)
    i += 1