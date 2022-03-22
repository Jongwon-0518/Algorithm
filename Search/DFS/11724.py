from sys import stdin
from collections import deque
import sys
sys.setrecursionlimit(10**6)

read = stdin.readline
n, m = map(int, read().split())
dic={}
for i in range(n):
    dic[i+1] = set()
for j in range(m):
    a, b = map(int, read().split())
    dic[a].add(b)
    dic[b].add(a)

def dfs(start, dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, dic)
            
visited = []
cnt = 0

for i in range(n):
    if i+1 not in visited:
        dfs(i+1, dic)
        cnt += 1

print(cnt)