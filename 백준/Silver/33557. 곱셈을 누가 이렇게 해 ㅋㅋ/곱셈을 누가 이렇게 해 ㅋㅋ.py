import sys
input_data = sys.stdin.read().split()

if input_data:
    t = int(input_data[0])
    current_index = 1
    
    for _ in range(t):
        a_str = input_data[current_index]
        b_str = input_data[current_index + 1]
        current_index += 2
        
        normal_val = str(int(a_str) * int(b_str))
        max_len = max(len(a_str), len(b_str))
        padded_a = a_str.rjust(max_len, '1')
        padded_b = b_str.rjust(max_len, '1')
        
        wrong_val_list = []
        for i in range(max_len):
            digit_a = int(padded_a[i])
            digit_b = int(padded_b[i])
            wrong_val_list.append(str(digit_a * digit_b))
            
        wrong_val = ''.join(wrong_val_list)
        
        if wrong_val == normal_val:
            print(1)
        else:
            print(0)