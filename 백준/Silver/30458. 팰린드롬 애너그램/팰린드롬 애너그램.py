from collections import Counter

n = int(input())
s = input()

half = n // 2
left = s[:half]
right = s[-half:]
left_count = Counter(left)
right_count = Counter(right)

total_count = Counter(s)

odd_count = sum(1 for c in total_count.values() if c % 2 == 1)
if (n % 2 == 0 and odd_count != 0) or (n % 2 == 1 and odd_count != 1):
    print('No')
    exit()

needed_left = Counter()
needed_right = Counter()

for ch, total in total_count.items():
    half_each = total // 2
    needed_left[ch] = half_each
    needed_right[ch] = half_each

for ch in total_count:
    l_have = left_count.get(ch, 0)
    r_have = right_count.get(ch, 0)
    l_need = needed_left[ch]
    r_need = needed_right[ch]

    if l_have + r_have < l_need + r_need:
        print('No')
        exit()

print('Yes')