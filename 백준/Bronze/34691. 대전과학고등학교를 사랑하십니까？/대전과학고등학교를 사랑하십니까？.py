import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    s = input()
    
    if s == 'end':
        break
    elif s == 'animal':
        print('Panthera tigris')
    elif s == 'tree':
        print('Pinus densiflora')
    elif s == 'flower':
        print('Forsythia koreana')