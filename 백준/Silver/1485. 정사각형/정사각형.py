import sys
input = lambda: sys.stdin.readline().rstrip()

def dist(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

result = []
for _ in range(int(input())):
    points = [tuple(map(int, input().split())) for _ in range(4)]
    dists = []
    for i in range(4):
        for j in range(i + 1, 4):
            dists.append(dist(points[i], points[j]))
    dists.sort()
    if dists[0] > 0 and dists[0] == dists[1] == dists[2] == dists[3] and dists[4] == dists[5] and dists[4] == 2 * dists[0]:
        result.append('1')
    else:
        result.append('0')
print('\n'.join(result))