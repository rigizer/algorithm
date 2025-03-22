n1, n2 = map(int, input().split())
ant1 = list(input())
ant2 = list(input())
t = int(input())

ants = ant1[::-1] + ant2
for _ in range(t):
    for i in range(len(ants)-1):
        if (ants[i] in ant1) and (ants[i+1] in ant2):
            ants[i], ants[i+1] = ants[i+1], ants[i]
            if ants[i+1] in ant1[0]:
                break
print(''.join(ants))