from sys import stdin

N, M = map(int, stdin.readline().split())

num = list(map(int, stdin.readline().split()))
for i in range(1, N):
    num[i] += num[i-1]
for _ in range(M):
    i, j = map(int, stdin.readline().split())
    if i>1:
        print(num[j-1]-num[i-2])
    else:
        print(num[j-1])