tier_order = {
    'B': 0,
    'S': 1,
    'G': 2,
    'P': 3,
    'D': 4
}

def parse(difficulty):
    tier = difficulty[0]
    level = int(difficulty[1:])
    return tier_order[tier] * 1000 + (1001 - level)

n = int(input())
difficulties = input().split()
values = [parse(x) for x in difficulties]
sorted_values = sorted(values)

if values == sorted_values:
    print('OK')
else:
    mismatch = [i for i in range(n) if values[i] != sorted_values[i]]
    
    i, j = mismatch
    wrong_pair = [difficulties[i], difficulties[j]]
    print('KO')
    print(*sorted(wrong_pair, key=parse))