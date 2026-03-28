import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    arr = list(map(int, input().split()))
    
    if arr[0] == 0:
        break
    
    n = arr[0]
    pitches = arr[1:]
    
    total = sum(pitches)
    max_pitch = max(pitches)
    
    result = []
    
    for L in [50, 60, 70]:
        if L < max_pitch or L < 2 * total:
            result.append('0')
        else:
            climbers = float('inf')
            
            for p in pitches:
                climbers = min(climbers, L // p + 1)
            
            result.append(str(climbers))
    
    print(' '.join(result))