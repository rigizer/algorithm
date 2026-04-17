import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    s = input()
    if s == '0':
        break

    nums = list(map(int, s.split('+')))
    buckets = [[] for _ in range(10)]

    for x in nums:
        buckets[x % 10].append(x)

    result = []
    for r in range(1, 5):
        while buckets[r] and buckets[10 - r]:
            result.append(buckets[r].pop())
            result.append(buckets[10 - r].pop())

    while len(buckets[0]) >= 2:
        result.append(buckets[0].pop())
        result.append(buckets[0].pop())

    while len(buckets[5]) >= 2:
        result.append(buckets[5].pop())
        result.append(buckets[5].pop())

    for r in range(10):
        while buckets[r]:
            result.append(buckets[r].pop())

    print('+'.join(map(str, result)))