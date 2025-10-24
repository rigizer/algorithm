import sys
input = lambda: sys.stdin.readline().rstrip()

def overlap(a, b, k):
    for i in range(k):
        if a[i:] == b[:k - i]:
            return k - i
    return 0

t = int(input())
for _ in range(t):
    k, w = map(int, input().split())
    words = [input() for _ in range(w)]
    
    result = k
    for i in range(1, w):
        ov = overlap(words[i - 1], words[i], k)
        result += (k - ov)
    
    print(result)