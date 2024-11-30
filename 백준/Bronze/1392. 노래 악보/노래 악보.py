n, q = map(int, input().split())

music_list = [int(input()) for _ in range(n)]
find_list = [int(input()) for _ in range(q)]

result = []
i = 1
for item in music_list:
    for _ in range(item):
        result.append(i)
    i = i + 1

for item in find_list:
    print(result[item])