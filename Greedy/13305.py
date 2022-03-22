from sys import stdin

n = int(stdin.readline().rstrip('\n'))
a = list(map(int, stdin.readline().split()))
b = list(map(int, stdin.readline().split()))

res = 0
m = b[0]
for i in range(n-1):
    if b[i] < m:
        m = b[i]
    res += m * a[i]

print(res)