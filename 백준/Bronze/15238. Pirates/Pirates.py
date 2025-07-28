n = int(input())
s = input()

cnt = {}
for c in s:
    cnt[c] = cnt.get(c, 0) + 1

ch = max(cnt, key=cnt.get)
print(ch, cnt[ch])