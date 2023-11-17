for i in range(int(input())):
    a, b, c, d, e, f = map(int,input().split())
    A, B, C, D, E, F, G = map(int,input().split())
    
    if a+2*b+3*c+3*d+4*e+10*f > A+2*B+2*C+2*D+3*E+5*F+10*G:
        print("Battle "+str(i+1)+": Good triumphs over Evil")
    elif a+2*b+3*c+3*d+4*e+10*f < A+2*B+2*C+2*D+3*E+5*F+10*G:
        print("Battle "+str(i+1)+": Evil eradicates all trace of Good")
    else:
        print("Battle "+str(i+1)+": No victor on this battle field")