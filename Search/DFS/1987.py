import sys
sys.setrecursionlimit(10**6)

R, C = map(int, sys.stdin.readline().split())
graph = []
for _ in range(R):
    graph.append(list(sys.stdin.readline().rstrip('\n')))
    
start = [0, 0]
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
visited = []
numlist = []

def dfs(start, graph, maxnum, numlist):
    if graph[start[0]][start[1]] not in visited:
        visited.append(graph[start[0]][start[1]])
        maxnum += 1
        numlist.append(maxnum)
    for di in dir:
        if start[0] + di[0] < 0 or start[0] + di[0] >= R or start[1] + di[1] < 0 or start[1] + di[1] >= C:
            pass
        elif graph[start[0]+di[0]][start[1]+di[1]] not in visited:
            dfs([start[0]+di[0],start[1]+di[1]], graph, maxnum, numlist)
    # for di in dir:
    #     try:
    #         if graph[start[0]+di[0]][start[1]+di[1]] not in visited:
    #             dfs([start[0]+di[0],start[1]+di[1]], graph, visited, maxnum, numlist)
    #     except:
    #         print('except')

dfs(start, graph, 0, numlist)
print(max(numlist))