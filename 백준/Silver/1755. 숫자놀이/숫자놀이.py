d = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', 
     '6':'six', '7':'seven', '8':'eight', '9':'nine', '0':'zero'}
m, n = map(int, input().split())
data = []
for i in range(m, n + 1):
    s = ' '.join([d[c] for c in str(i)])
    data.append([i, s])

data.sort(key=lambda x:x[1])

for i in range(len(data)):
    if i % 10 == 0 and i!= 0:
        print()
    print(data[i][0], end=' ')