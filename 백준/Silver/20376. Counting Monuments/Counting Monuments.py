import sys
input = lambda: sys.stdin.readline().rstrip()

monuments = set()

for line in sys.stdin:
    if not line:
        break
    _, name = line.split(' ', 1)
    monuments.add(name)

print(len(monuments))