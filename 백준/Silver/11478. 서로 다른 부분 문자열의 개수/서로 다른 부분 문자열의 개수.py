s = input()
cnt = set()
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        cnt.add(s[i:j])
print(len(cnt))