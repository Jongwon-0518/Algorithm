from sys import stdin
import heapq

N, M, X = map(int, stdin.readline().split())

dic = {}

for _ in range(M):
    a, b, t = map(int, stdin.readline().split())
    if a in dic:
        dic[a].append((b, t))
    else:
        dic[a] = [(b, t)]

def bfs(i, j):
    queue = [(0, i)]
    heapq.heapify(queue)
    visited = [False]*(N+1)
    while queue:
        cnt, node = heapq.heappop(queue)
        visited[node] = True
        if node==j:
            return cnt
        else:
            if node in dic:
                for t in dic[node]:
                    if not visited[t[0]]:
                        heapq.heappush(queue, (cnt+t[1], t[0]))

answer = []

for i in range(1, N+1):
    answer.append(bfs(i, X)+bfs(X, i))

print(max(answer))