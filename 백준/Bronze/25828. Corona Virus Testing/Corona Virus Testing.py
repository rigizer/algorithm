g, p, t = map(int, input().split())
individual_kits = g * p
group_kits = g + (t * p)

if individual_kits < group_kits:
    print(1)
elif individual_kits > group_kits:
    print(2)
else:
    print(0)