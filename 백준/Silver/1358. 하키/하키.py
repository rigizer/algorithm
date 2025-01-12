def is_inside_rink(W, H, X, Y, a, b):
    if X <= a <= X + W and Y <= b <= Y + H:
        return 1
    left_circle_center = (X, Y + H / 2)
    if ((a - left_circle_center[0]) ** 2 + (b - left_circle_center[1]) ** 2) <= (H / 2) ** 2:
        return 1
    right_circle_center = (X + W, Y + H / 2)
    if ((a - right_circle_center[0]) ** 2 + (b - right_circle_center[1]) ** 2) <= (H / 2) ** 2:
        return 1
    return 0

W, H, X, Y, P = map(int, input().split())
result = 0

for _ in range(P):
    a, b = map(int, input().split())
    result += is_inside_rink(W, H, X, Y, a, b)

print(result)