from sys import stdin
read = stdin.readline
i = 1000 - int(read())

k = [500, 100, 50, 10, 5, 1]
cnt = 0

for j in k:
    a = i//j
    i -= a*j
    cnt += a

print(cnt)