from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
dic_a = {}
dic_b = {}
for _ in range(N):
    x, y = map(int, stdin.readline().split())
    dic_a[x] = y
for _ in range(M):
    u, v = map(int, stdin.readline().split())
    dic_b[u] = v

queue = deque([(0, 1)])
answer = 0
visited = [False]*101
while queue:
    cnt, node = queue.popleft()

    if node==100:
        print(cnt)
        break
    next_cnt = cnt+1
    for i in range(1, 7):
        next_node = node+i

        if next_node<=100 and not visited[next_node]:
            if next_node in dic_a:
                next_node = dic_a[next_node]
            if next_node in dic_b:
                next_node = dic_b[next_node]
            
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((next_cnt, next_node))