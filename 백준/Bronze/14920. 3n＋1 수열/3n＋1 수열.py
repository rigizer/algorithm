n = int(input())
count = 0

while True :
  if n == 1 :
    count += 1
    break
  if n % 2 == 0 :
    n //= 2
    count += 1
  else :
    n = 3 * n + 1
    count += 1

print(count)