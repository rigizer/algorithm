def next_char(c, offset):
    return chr((ord(c) - ord('A') + offset) % 26 + ord('A'))

n = int(input())
for i in range(n):
    parts = input().split()
    size = int(parts[0]) if parts[0].isdigit() else int(parts[1])
    ch = parts[1] if parts[0].isdigit() else parts[0]
    
    for j in range(size):
        current_char = next_char(ch, j)
        print(current_char * (j + 1))
    if i != n - 1:
        print()