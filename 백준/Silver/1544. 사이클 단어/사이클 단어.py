from collections import deque

def rotate_word(w1, w2):
    if len(w1)!=len(w2): return w2
    w2 = deque(w2)
    
    for _ in range(len(w2)):
        w2.rotate(1)
        t = ''.join(w2)
        if w1==t: return t
    
    return ''.join(w2)


n = int(input())
l = [input() for _ in range(n)]

for i in range(n):
    for j in range(i,n):
        if l[i]!=l[j]:
            l[j] = rotate_word(l[i], l[j])

print(len(set(l)))