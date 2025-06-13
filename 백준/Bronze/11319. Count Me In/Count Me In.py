vowels_set = set('aeiouAEIOU')

s = int(input())
for _ in range(s):
    line = input()
    vowel_count = 0
    consonant_count = 0

    for ch in line:
        if ch.isalpha():
            if ch in vowels_set:
                vowel_count += 1
            else:
                consonant_count += 1

    print(f'{consonant_count} {vowel_count}')