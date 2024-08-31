while True:
    try:
        ss = input()
        if not ss:
            break
        s, t = ss.split()
        flag = 0
        idx = 0
    
        for i in range(len(t)):
            if t[i] == s[idx]:
                idx += 1
                if idx == len(s):
                    flag = 1
                    break
    
        print('Yes' if flag == 1 else 'No')
    except:
        break