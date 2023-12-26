a, b = map(str, input().split())
a, b = [int(i) for i in a], [int(i) for i in b]
print(sum(a) * sum(b))