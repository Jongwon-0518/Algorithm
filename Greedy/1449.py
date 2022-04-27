import sys

N, L = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
data.sort()
ans = 0
matrix = [0]*N

for i in range(N):
    if matrix[i]==0:
        matrix[i]=1
        ans += 1
        for j in range(i+1, N):
            if data[j] - data[i] < L:
                matrix[j] = 1

print(ans)