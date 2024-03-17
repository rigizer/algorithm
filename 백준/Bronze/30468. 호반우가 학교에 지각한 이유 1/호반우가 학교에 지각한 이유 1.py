STR, DEX, INT, LUK, N = map(int, input().split())

s = STR + DEX + INT + LUK
ts = N * 4

print(ts - s if ts - s > 0 else 0)