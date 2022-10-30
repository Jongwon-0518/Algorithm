from sys import stdin
import sys
sys.setrecursionlimit(10**9)

n = int(stdin.readline())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    s, e, w = map(int, stdin.readline().split())
    graph[e].append([s, w])
    graph[s].append([e, w])


def dfs(x, wei):
    for i in graph[x]:
        a, b = i
        if dist[a] == -1:
            dist[a] = wei+b
            dfs(a, wei+b)


dist = [-1]*(n+1)
dist[1] = 0
dfs(1, 0)

start = dist.index(max(dist))
dist = [-1]*(n+1)
dist[start] = 0
dfs(start, 0)

print(max(dist))
