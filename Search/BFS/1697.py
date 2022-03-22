from sys import stdin
from collections import deque

N, K = map(int, stdin.readline().split())
queue = deque()
queue.append(N)
MAX = 10**5
dist = [0]*(MAX+1)

while queue:
    x = queue.popleft()
    if x == K:
        print(dist[x])
        break
    for nx in (x-1, x+1, x*2):
        if 0<=nx<=MAX and not dist[nx]:
            dist[nx] = dist[x] + 1
            queue.append(nx)
