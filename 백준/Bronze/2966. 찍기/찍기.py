A, B, G = 0, 0, 0
n = int(input())
correct = input()
for i in range(n):
    if i % 3 == 0:
        if correct[i] == 'A':
            A += 1
    elif i % 3 == 1:
        if correct[i] == 'B':
            A += 1
    else:
        if correct[i] == 'C':
            A += 1
            
    if i % 4 == 0 or i % 4 == 2:
        if correct[i] == 'B':
            B += 1
    elif i % 4 == 1:
        if correct[i] == 'A':
            B += 1
    else:
        if correct[i] == 'C':
            B += 1
            
    if i % 6 == 0 or i % 6 == 1:
        if correct[i] == 'C':
            G += 1
    elif i % 6 == 2 or i % 6 == 3:
        if correct[i] == 'A':
            G += 1
    else:
        if correct[i] == 'B':
            G += 1
            
m = max(A, B, G)
print(m)
if m == A:
    print('Adrian')
if m == B:
    print('Bruno')
if m == G:
    print('Goran')