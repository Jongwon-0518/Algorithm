from sys import stdin

N, M = map(int, stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, stdin.readline().split())))
answer = set()

def op1(x, y):
    if y<=M-4:
        answer.add(sum(graph[x][y:y+4]))
    if x<=N-4:
        answer.add(graph[x][y]+graph[x+1][y]+graph[x+2][y]+graph[x+3][y])

def op2(x, y):
    if x<N-1 and y<M-1:
        answer.add(sum(graph[x][y:y+2])+sum(graph[x+1][y:y+2]))

def op3(x, y):
    if x>=1 and y<=M-3:
        answer.add(sum(graph[x][y:y+3])+graph[x-1][y+2])
    if x>=1 and y<=M-3:
        answer.add(sum(graph[x][y:y+3])+graph[x-1][y])
    if x<N-1 and y<=M-3:
        answer.add(sum(graph[x][y:y+3])+graph[x+1][y])
    if x<N-1 and y<=M-3:
        answer.add(sum(graph[x][y:y+3])+graph[x+1][y+2])
    if x<=N-3 and y<M-1:
        answer.add(graph[x][y]+graph[x+1][y]+graph[x+2][y]+graph[x+2][y+1])
    if x<=N-3 and y>=1:
        answer.add(graph[x][y]+graph[x+1][y]+graph[x+2][y]+graph[x+2][y-1])
    if x<=N-3 and y<M-1:
        answer.add(graph[x][y]+graph[x+1][y]+graph[x+2][y]+graph[x][y+1])
    if x<=N-3 and y>=1:
        answer.add(graph[x][y]+graph[x+1][y]+graph[x+2][y]+graph[x][y-1])
    
def op4(x, y):
    if x<=N-3 and y<M-1:
        answer.add(graph[x][y]+graph[x+1][y]+graph[x+1][y+1]+graph[x+2][y+1])
    if x<=N-3 and y>=1:
        answer.add(graph[x+2][y-1]+graph[x+1][y-1]+graph[x+1][y]+graph[x][y])
    if x>=1 and y<=M-3:
        answer.add(sum(graph[x][y:y+2])+sum(graph[x-1][y+1:y+3]))
    if x<N-1 and y<=M-3:
        answer.add(sum(graph[x][y:y+2])+sum(graph[x+1][y+1:y+3]))

def op5(x, y):
    if x<N-1 and y<=M-3:
        answer.add(sum(graph[x][y:y+3])+graph[x+1][y+1])
    if x>=1 and y<=M-3:
        answer.add(sum(graph[x][y:y+3])+graph[x-1][y+1])
    if x<=N-3 and y>=1:
        answer.add(graph[x][y]+graph[x+1][y]+graph[x+1][y-1]+graph[x+2][y])
    if x<=N-3 and y<M-1:
        answer.add(graph[x][y]+graph[x+1][y]+graph[x+1][y+1]+graph[x+2][y])

    
for i in range(N):
    for j in range(M):
        op1(i, j)
        op2(i, j)
        op3(i, j)
        op4(i, j)
        op5(i, j)

print(max(answer))