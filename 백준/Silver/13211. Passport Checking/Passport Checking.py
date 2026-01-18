import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
stolen_passports = set()

for _ in range(n):
    stolen_passports.add(input())

m = int(input())
result = 0

for _ in range(m):
    passport = input()
    if passport in stolen_passports:
        result += 1

print(result)