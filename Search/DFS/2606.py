from sys import stdin
# graph형식으로 데이터 저장
read = stdin.readline
dic={}
for i in range(int(read())):
    dic[i+1] = set()
for j in range(int(read())):
    a, b = map(int, read().split())
    dic[a].add(b)
    dic[b].add(a)

# dfs
def dfs(start, dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, dic)
# 방문 여부
visited = []

dfs(1, dic)
print(len(visited)-1)