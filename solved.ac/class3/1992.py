from sys import stdin

N = int(stdin.readline())
data = []
for _ in range(N):
    data.append(list(map(int, str(stdin.readline().rstrip()))))

def check(graph):
    for i in range(len(graph)):
        for j in range((len(graph))):
            if graph[i][j] != graph[0][0]:
                return False
    return True


res = ""
def function(graph, ori):
    global res
    if check(graph):
        res += str(graph[0][0])
    else:
        res += '('
        k = len(graph)//2
        for i in range(2):
            x = k*i
            for j in range(2):
                y = k*j
                new_graph = [[0]*k for _ in range(k)]
                for a in range(x, x+k):
                    for b in range(y, y+k):
                        new_graph[a-x][b-y] = graph[a][b]
                function(new_graph, [i, j])
        res += ')'

function(data, [2, 2])

print(res)