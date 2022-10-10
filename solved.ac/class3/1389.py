from sys import stdin
from collections import deque

N, M  = map(int, stdin.readline().split())

data = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, stdin.readline().split())
    data[a].append(b)
    data[b].append(a)

def bfs(a):
    queue = deque([a])
    visited[a] = 1

    
    while queue:
        target = queue.popleft()

        for i in data[target]:
            if not visited[i]:
                visited[i] = visited[target] +1
                queue.append(i)

answer = []
for i in range(1, N+1):
    visited = [0]*(N+1)
    bfs(i)
    answer.append(sum(visited))

print(answer.index(min(answer))+1)