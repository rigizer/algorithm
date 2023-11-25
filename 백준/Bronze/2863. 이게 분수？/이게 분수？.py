a, b = map(int , input().split())
c, d = map(int , input().split())
l = [a/c + b/d, c/d + a/b, d/b + c/a, b/a + d/c]
print(l.index(max(l)))