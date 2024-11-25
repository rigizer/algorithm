n = int(input())

for i in range(0, n):
    a = input()
    a = a.replace(' ', '')

    s1 = set(a)
    s2 = list(s1)

    s2_cnt = []

    for j in range(0, len(s2)):
        s2_cnt.append(a.count(s2[j]))
    
    m = max(s2_cnt)

    if s2_cnt.count(m) > 1:
        print('?')
    else:
        m2 = s2_cnt.index(m)
        print(s2[m2])