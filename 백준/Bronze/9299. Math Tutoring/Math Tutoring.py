t = int(input())

for case in range(1, t + 1):
    data = list(map(int, input().split()))
    n = data[0]
    coeffs = data[1:]

    result = []
    for i in range(len(coeffs) - 1):
        exp = n - i
        result.append(coeffs[i] * exp)

    print('Case {}: {} {}'.format(case, n - 1, ' '.join(map(str, result))))