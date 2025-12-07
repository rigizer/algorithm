import sys
input = lambda: sys.stdin.readline().rstrip()

mirror_map = {
    'A':'A','E':'3','3':'E','H':'H','I':'I','J':'L','L':'J',
    'M':'M','O':'O','S':'2','2':'S','T':'T','U':'U','V':'V',
    'W':'W','X':'X','Y':'Y','Z':'5','5':'Z','1':'1','8':'8'
}

def is_palindrome(s):
    return s == s[::-1]

def is_mirrored(s):
    t = []
    for c in s:
        if c not in mirror_map:
            return False
        t.append(mirror_map[c])
    t = ''.join(t)[::-1]
    return t == s

first = True
for line in sys.stdin:
    s = line.rstrip()

    if not first:
        print()
    first = False

    p = is_palindrome(s)
    m = is_mirrored(s)

    if p and m:
        print(s + ' -- is a mirrored palindrome.')
    elif p:
        print(s + ' -- is a palindrome.')
    elif m:
        print(s + ' -- is a mirrored string.')
    else:
        print(s + ' -- is not a palindrome.')