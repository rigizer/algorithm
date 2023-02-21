def get_gcd(a, b):
    for i in range(min(a, b), 1, -1):
        if a % i == 0 and b % i == 0:
            return i
    
    return 1

def get_lcm(a, b, gcd):
    return a * b // gcd

a, b = map(int, input().split())

# 최대공약수
gcd = get_gcd(a, b)
print(gcd)

# 최소공배수
lcm = get_lcm(a, b, gcd)
print(lcm)