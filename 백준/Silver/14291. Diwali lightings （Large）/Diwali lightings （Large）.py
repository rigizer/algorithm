def calc(s, i, j):
    length = len(s)
    blue_count = s.count('B')
    total_len = j - i + 1

    start_idx = (i - 1) % length
    full_patterns = total_len // length
    remainder = total_len % length
    result = full_patterns * blue_count

    for k in range(remainder):
        if s[(start_idx + k) % length] == 'B':
            result += 1

    return result

t = int(input())
for case_num in range(1, t + 1):
    s = input().strip()
    i, j = map(int, input().split())
    result = calc(s, i, j)
    print(f'Case #{case_num}: {result}')