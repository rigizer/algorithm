answer = 0
while True:
    line = input()
    if line == '고무오리 디버깅 끝':
        break
    
    if line == '문제':
        answer += 1
    elif line == '고무오리' and answer == 0:
        answer += 2
    elif line == '고무오리':
        answer -= 1

if answer == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')