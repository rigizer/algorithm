n = input()
length = len(n)

is_yujin = False

for i in range(1, length):
    left = n[:i]
    right = n[i:]
    
    left_product = 1
    right_product = 1
    
    for digit in left:
        left_product *= int(digit)
        
    for digit in right:
        right_product *= int(digit)
        
    if left_product == right_product:
        is_yujin = True
        break

if is_yujin:
    print('YES')
else:
    print('NO')