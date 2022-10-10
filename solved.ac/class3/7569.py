from sys import stdin
from collections import deque

M, N, H = map(int, stdin.readline().split())
graph = [[[] for _ in range(N)] for _ in range(H)]
for i in range(H):
    for j in range(N):
        graph[i][j] = list(map(int, stdin.readline().split()))
tomato = []
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k]==1:
                tomato.append([i, j, k, 0])

queue = deque(tomato)

dh, dn, dm = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]
answer = []



while queue:
    x = queue.popleft()
    answer.append(x[3])
    for i in range(6):
        nh, nn, nm = x[0]+dh[i], x[1]+dn[i], x[2]+dm[i]

        if 0<=nh<H and 0<=nn<N and 0<=nm<M and graph[nh][nn][nm]==0:
            graph[nh][nn][nm]=1
            queue.append([nh, nn, nm, x[3]+1])

t=False
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k]==0:
                break
        if graph[i][j][k]==0:
            break
    if graph[i][j][k]==0:
        t = True
        break
if t:
    print(-1)
else:
    print(max(answer))