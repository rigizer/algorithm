cn = [i ** 2 for i in range(31623)]
result = ['1' if (int(input()) in cn) else '0' for _ in range(int(input()))]
print('\n'.join(result))