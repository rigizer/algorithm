import sys
input = lambda: sys.stdin.readline().rstrip()

s = input()

nums = set()
current = ''

for ch in s:
    if ch.isdigit():
        current += ch
    else:
        if current:
            nums.add(int(current))
            current = ''

if current:
    nums.add(int(current))

print(len(nums))