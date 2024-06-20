for _ in range(1, int(input()) + 1) :
    N, D, A, B, F = map(float, input().split())
    print(int(N), D / (A + B) * F)