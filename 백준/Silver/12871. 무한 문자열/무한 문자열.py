import math

s, t = input(), input()
lcm_len = (len(s) * len(t)) // math.gcd(len(s), len(t))
if s * (lcm_len // len(s)) == t * (lcm_len // len(t)):
    result = 1
else:
    result = 0
print(result)