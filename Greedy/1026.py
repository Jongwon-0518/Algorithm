from audioop import reverse
from sys import stdin

read = stdin.readline
n = int(read())
a = list(map(int, read().split()))
b = list(map(int, read().split()))

a.sort()
b.sort(reverse=True)

sum = 0

for i in range(n):
    sum += a[i]*b[i]

print(sum)