from sys import stdin
import heapq
import sys

INF = sys.maxsize

N = int(stdin.readline())

M = int(stdin.readline())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, t = map(int, stdin.readline().split())
    graph[s].append((e, t))

v1, v2 = map(int, stdin.readline().split())

def dijkstra(s, e):
    dis = [INF]*(N+1)
    q = []
    heapq.heapify(q)
    heapq.heappush(q, (0, s))
    while q:
        cnt, node = heapq.heappop(q)
        if node == e:
            return cnt
        if dis[node] > cnt:
            dis[node] = cnt
            if graph[node]:
                for i in graph[node]:
                    if dis[i[0]] > cnt+i[0]:
                        heapq.heappush(q, (cnt+i[1], i[0]))

print(dijkstra(v1, v2))