import sys
input = lambda: sys.stdin.readline().rstrip()

def is_right_triangle(sides):
    sides.sort()
    a, b, c = sides
    return a * a + b * b == c * c, (a, b)

n = int(input())
result = []
for _ in range(n):
    t1 = list(map(int, input().split()))
    t2 = list(map(int, input().split()))
    r1, legs1 = is_right_triangle(t1)
    r2, legs2 = is_right_triangle(t2)
    if r1 and r2 and set(legs1) == set(legs2):
        result.append('YES')
    else:
        result.append('NO')
print('\n'.join(result))