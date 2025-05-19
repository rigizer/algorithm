def round(n):return int(n+0.5)
n=int(input())
if n==0: print(0);exit()
ns=sorted([int(input()) for _ in range(n)])
a=ns[round(n*0.15):n-round(n*0.15)]
print(round(sum(a)/len(a)))