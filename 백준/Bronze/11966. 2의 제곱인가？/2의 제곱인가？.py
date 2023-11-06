n = int(input())
s = [2 ** i for i in range(31)]
print(1 if n in s else 0)