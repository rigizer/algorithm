import sys
input = lambda: sys.stdin.readline().rstrip()

def recursion(s, left, right, counter):
    counter[0] += 1
    
    if left >= right:
        return 1
    else:
        if s[left] != s[right]:
            return 0
        else:
            return recursion(s, left + 1, right - 1, counter)

def is_palindrome(s):
    counter = [0]
    result = recursion(s, 0, len(s) - 1, counter)
    return result, counter[0]

t = int(input())
outputs = []
for _ in range(t):
    s = input()
    result, count = is_palindrome(s)
    outputs.append(f'{result} {count}')

print('\n'.join(outputs))