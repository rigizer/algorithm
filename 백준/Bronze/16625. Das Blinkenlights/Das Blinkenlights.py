import math
p, q, s = map(int, input().split())
lcm = p * q // math.gcd(p, q)
print('yes' if lcm <= s else 'no')