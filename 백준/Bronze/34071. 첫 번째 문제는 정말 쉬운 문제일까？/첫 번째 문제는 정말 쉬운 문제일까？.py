n = int(input())
q = [int(input()) for _ in range(n)]
print('ez' if min(q) == q[0] else ('hard' if max(q) == q[0] else '?'))