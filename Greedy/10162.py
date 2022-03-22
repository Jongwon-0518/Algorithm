from sys import stdin
read = stdin.readline
i = int(read())

k = [300, 60, 10]
l = [0, 0, 0]

for j in range(3):
    a = i//k[j]
    i -= a*k[j]
    l[j] = a

if i%10 == 0:
    for t in range(3):
        print(l[t], end=' ')
else:
    print(-1)
