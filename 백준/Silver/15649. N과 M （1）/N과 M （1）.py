n, m = map(int, input().split())
visited = [False] * (n + 1)
sequence = []

def num(depth):
    if depth == m:
        print(*sequence)
        return
    
    for i in range(1, n + 1): 
        if not visited[i]:
            visited[i] = True
            sequence.append(i)
            num(depth + 1)
            sequence.pop()
            visited[i] = False

num(0)