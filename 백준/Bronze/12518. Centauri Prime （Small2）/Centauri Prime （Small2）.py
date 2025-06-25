t = int(input())
vowels = {'a', 'e', 'i', 'o', 'u'}

for i in range(1, t + 1):
    country = input()
    last_char = country[-1].lower()
    
    if last_char == 'y':
        ruler = 'nobody'
    elif last_char in vowels:
        ruler = 'a queen'
    else:
        ruler = 'a king'
    
    print(f'Case #{i}: {country} is ruled by {ruler}.')