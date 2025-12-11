import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    music = input()
    
    if music == '#':
        break
    
    for i, v in enumerate(music):
        if i == 0:
            continue
        
        if (ord(music[i]) - ord(music[i - 1])) % 7 not in (2, 4, 6):
            print('Ouch! That hurts my ears.')
            break
    else:    
        print('That music is beautiful.')