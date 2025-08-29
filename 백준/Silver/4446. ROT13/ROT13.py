import sys

vowels = 'aiyeou'
vowels_upper = vowels.upper()
consonants = 'bkxznhdcwgpvjqtsrlmf'
consonants_upper = consonants.upper()

for line in sys.stdin:
    line = line.rstrip('\n')
    result = ''
    for ch in line:
        if ch in vowels:
            idx = vowels.index(ch)
            result += vowels[(idx + 3) % len(vowels)]
        elif ch in vowels_upper:
            idx = vowels_upper.index(ch)
            result += vowels_upper[(idx + 3) % len(vowels_upper)]
        elif ch in consonants:
            idx = consonants.index(ch)
            result += consonants[(idx + 10) % len(consonants)]
        elif ch in consonants_upper:
            idx = consonants_upper.index(ch)
            result += consonants_upper[(idx + 10) % len(consonants_upper)]
        else:
            result += ch
    print(result)