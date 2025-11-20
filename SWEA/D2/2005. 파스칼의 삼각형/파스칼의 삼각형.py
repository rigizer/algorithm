tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    graph = [[1] * (i + 1) for i in range(n)]
    
    for i in range(2, n):
        for j in range(1, i):
            graph[i][j] = graph[i - 1][j - 1] + graph[i - 1][j]
    
    print(f"#{t}")
    for row in graph:
        print(*row)