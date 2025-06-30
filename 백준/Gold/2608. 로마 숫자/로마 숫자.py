def roman_to_int(s):
    roman = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }
    special = {
        'IV': 4, 'IX': 9,
        'XL': 40, 'XC': 90,
        'CD': 400, 'CM': 900
    }
    i = 0
    total = 0
    while i < len(s):
        if i + 1 < len(s) and s[i:i+2] in special:
            total += special[s[i:i+2]]
            i += 2
        else:
            total += roman[s[i]]
            i += 1
    return total

def int_to_roman(n):
    vs = [
        (1000, 'M'), (900, 'CM'),
        (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'),
        (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'),
        (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]
    result = ''
    for v, s in vs:
        while n >= v:
            result += s
            n -= v
    return result

s1, s2 = input(), input()
n1 = roman_to_int(s1)
n2 = roman_to_int(s2)
total = n1 + n2

print(total)
print(int_to_roman(total))