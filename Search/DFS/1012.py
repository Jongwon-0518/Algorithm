from sys import stdin
# 백준 제출시 재귀함수로 인한 에러가 뜰시 추가
import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if t[x][y]==1:
        t[x][y]=0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

read = stdin.readline
a = []
b = int(read())

for _ in range(b):
    result = 0
    m, n, k = map(int, read().split())
    t = [[0] * m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, read().split())
        t[x][y] = 1
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1
    a.append(result)
    
for k in range(b):
    print(a[k])