keyboard = [[], ['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'],
                ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
p, w = map(int, input().split())
text = input()

total = 0
past_j = ''
for i in range(len(text)):
    if text[i] == ' ':
        total += p
        past_j = ''
    for j in range(len(keyboard)):
        for k in range(len(keyboard[j])):
            if text[i] == keyboard[j][k]:
                if j == past_j:
                    total += w
                total += (1+k) * p
                past_j = j
print(total)