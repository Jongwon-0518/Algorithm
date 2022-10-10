from sys import stdin

N = int(stdin.readline())
data = []
for _ in range(N):
    data.append(list(map(int, stdin.readline().split())))

def check(graph):
    for i in range(len(graph)):
        for j in range((len(graph))):
            if graph[i][j] != graph[0][0]:
                return False
    return True

dic = {}
for i in range(3):
    dic[i-1] = 0

def function(graph):
    if check(graph):
        dic[graph[0][0]] += 1
    else:
        k = len(graph)//3
        for i in range(3):
            x = k*i
            for j in range(3):
                y = k*j
                new_graph = [[0]*k for _ in range(k)]
                for a in range(x, x+k):
                    for b in range(y, y+k):
                        new_graph[a-x][b-y] = graph[a][b]
                function(new_graph)


function(data)

for i in range(3):
    print(dic[i-1])