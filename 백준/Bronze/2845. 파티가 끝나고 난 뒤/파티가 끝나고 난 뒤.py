l, p = map(int, input().split())
n = list(map(int, input().split()))
print(' '.join([str(i - l * p) for i in n]))