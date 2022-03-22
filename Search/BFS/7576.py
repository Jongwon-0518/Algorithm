from sys import stdin
# bfs특 queue 사용, deque 모듈 안쓰면 시간 복잡도 박살남
from collections import deque

m, n = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
res = 0
queue = deque([])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

# while로 인해 재귀할 필요없이 다 돌고 나옴
def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])    

bfs()
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))

print(res - 1)