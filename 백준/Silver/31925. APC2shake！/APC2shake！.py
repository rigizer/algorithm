import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
candidates = []

for _ in range(n):
    name, enroll, icpc, s_str, a_str = input().split()
    s = int(s_str)
    a = int(a_str)

    if enroll != 'jaehak':
        continue
    if icpc != 'notyet':
        continue
    if not (s == -1 or s > 3):
        continue

    candidates.append((a, name))

candidates.sort()
selected = candidates[:10]

names = [name for _, name in selected]
names.sort()

print(len(names))
for name in names:
    print(name)