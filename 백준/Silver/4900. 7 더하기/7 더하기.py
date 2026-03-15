import sys
input = lambda: sys.stdin.readline().rstrip()

code_to_digit = {
    '063': '0',
    '010': '1',
    '093': '2',
    '079': '3',
    '106': '4',
    '103': '5',
    '119': '6',
    '011': '7',
    '127': '8',
    '107': '9'
}

digit_to_code = {v: k for k, v in code_to_digit.items()}

while True:
    line = input()
    
    if line == 'BYE':
        break
    
    left, right = line.split('+')
    b = right[:-1]
    
    a_num = ''
    for i in range(0, len(left), 3):
        a_num += code_to_digit[left[i:i+3]]
    
    b_num = ''
    for i in range(0, len(b), 3):
        b_num += code_to_digit[b[i:i+3]]
    
    c = str(int(a_num) + int(b_num))
    
    c_code = ''
    for ch in c:
        c_code += digit_to_code[ch]
    
    print(left + '+' + b + '=' + c_code)