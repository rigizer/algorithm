import sys
input = lambda: sys.stdin.readline().rstrip()

h = int(input())
m = int(input())

nums = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
    7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'quarter', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
    21: 'twenty one', 22: 'twenty two', 23: 'twenty three',
    24: 'twenty four', 25: 'twenty five', 26: 'twenty six',
    27: 'twenty seven', 28: 'twenty eight', 29: 'twenty nine',
    30: 'half'
}

if m == 0:
    print(f"{nums[h]} o' clock")
elif m == 15:
    print(f'quarter past {nums[h]}')
elif m == 30:
    print(f'half past {nums[h]}')
elif m < 30:
    unit = 'minute' if m == 1 else 'minutes'
    print(f'{nums[m]} {unit} past {nums[h]}')
else:
    mm = 60 - m
    nh = h + 1 if h < 12 else 1
    if mm == 15:
        print(f'quarter to {nums[nh]}')
    else:
        unit = 'minute' if mm == 1 else 'minutes'
        print(f'{nums[mm]} {unit} to {nums[nh]}')