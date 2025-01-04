def jinsu(a,b):
    tmp=[]
    while a>0:
        tmp.append(a%b)
        a=a//b
    tmp=tmp[::-1]
    return tmp
def chk(s):
    for i in range(len(s)//2):
        if s[i]!= s[-i-1]:
            return False
    return True
t=int(input())
for _ in range(t):
    cnt=False
    n=int(input())
    for i in range(2,65):
        if chk(jinsu(n, i)):
            cnt=chk(jinsu(n,i))
            break
    if cnt : print(1)
    else: print(0)