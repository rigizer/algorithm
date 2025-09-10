import sys

vowel = set('aeiouAEIOU')
result = []
for line in sys.stdin:
    word = line.strip().split()
    vowel_word = [w for w in word if w[0] in vowel][::-1]
    idx = 0
    new_line = []
    for w in word:
        if w[0] in vowel:
            new_line.append(vowel_word[idx])
            idx += 1
        else:
            new_line.append(w)
    result.append(' '.join(new_line))

print('\n'.join(result))