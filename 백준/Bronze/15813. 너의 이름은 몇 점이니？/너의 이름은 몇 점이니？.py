count = int(input())
name = list(input())
print(sum([ord(i) - 64 for i in name]))