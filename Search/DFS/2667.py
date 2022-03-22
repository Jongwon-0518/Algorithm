def dfs(x, y):
    if x<=-1 or x>=n or y<=-1 or y>=n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        global count
        count += 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

count = 0
c =[]
result = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result += 1
            c.append(count)
            count = 0
c.sort()
print(result)
for i in range(result):
    print(c[i])