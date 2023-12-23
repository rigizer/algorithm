a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_cnt, b_cnt = 0, 0
 
for a_card, b_card in zip(a, b):
    if a_card > b_card:
        a_cnt += 1
    elif a_card < b_card:
        b_cnt += 1
 
if a_cnt > b_cnt:
    print('A')
elif a_cnt < b_cnt:
    print('B')
else:
    print('D')