n, m = map(int, input().split())
sequence = []

def backtrack(start):
    if len(sequence) == m:
        print(*sequence)
        return
    
    for i in range(start, n + 1):
        sequence.append(i)
        backtrack(i + 1)
        sequence.pop()

backtrack(1)