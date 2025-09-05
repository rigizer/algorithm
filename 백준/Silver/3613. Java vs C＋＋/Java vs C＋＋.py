import sys
input = lambda: sys.stdin.readline().rstrip()

s = input()
if not s:
    print('Error!')
    sys.exit()

def is_c_style(t):
    if any(c.isupper() for c in t): return False
    if t[0] == '_' or t[-1] == '_': return False
    if '__' in t: return False
    return True

def is_java_style(t):
    if '_' in t: return False
    if t[0].isupper(): return False
    return True

if ('_' in s) and any(c.isupper() for c in s):
    print('Error!')
elif is_c_style(s) and not is_java_style(s):
    parts = s.split('_')
    print(parts[0] + ''.join(p.capitalize() for p in parts[1:]))
elif is_java_style(s):
    res = []
    for c in s:
        if c.isupper():
            res.append('_')
            res.append(c.lower())
        else:
            res.append(c)
    print(''.join(res))
else:
    print('Error!')