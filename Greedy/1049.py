from sys import stdin

N, M = map(int, stdin.readline().split())
set = []
each = []
price = []
for _ in range(M):
    a, b = map(int, stdin.readline().split())
    set.append(a)
    each.append(b)
set.sort()
each.sort()
a = N//6
b = N-a*6
price.append(set[0]*(a+1))
price.append(set[0]*a+b*each[0])
price.append(N*each[0])
print(min(price))