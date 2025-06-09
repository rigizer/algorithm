def convert(m, n):
    digits = '0123456789ABCDEF'
    if m == 0:
        return '0'
    
    result = ''
    while m > 0:
        result = digits[m % n] + result
        m //= n
    return result

m, n = map(int, input().split())
print(convert(m, n))