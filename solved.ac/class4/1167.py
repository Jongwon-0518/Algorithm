import sys
from collections import deque

V = int(sys.stdin.readline().rstrip())
data = [[] for _ in range(V+1)]

for _ in range(V):
    a = list(map(int, sys.stdin.readline().split()))
    for e in range(1, len(a)-2, 2):
        data[a[0]].append((a[e], a[e+1]))

def bfs(start):
    visit=[-1]*(V+1)
    que=deque()
    que.append(start)
    visit[start]=0
    _max=[0, 0]

    while que:
        t=que.popleft()
        for e, w in data[t]:
            if visit[e]==-1:
                visit[e]=visit[t]+w
                que.append(e)
                if _max[0] < visit[e]:
                    _max=visit[e], e
    
    return _max

dis, node = bfs(1)
dis, node = bfs(node)
print(dis)