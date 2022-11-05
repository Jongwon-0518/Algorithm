from sys import stdin

n, m = map(int, stdin.readline().split())

a, b = 1, 1

for i in range(1, m+1):
    b *= i
    a *= n+1-i

answer = a//b

print(answer)