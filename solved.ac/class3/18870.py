import sys

N = int(sys.stdin.readline().rstrip())
data=list(map(int, sys.stdin.readline().split()))
graph = sorted(list(set(data)))
dic = {graph[i] : i for i in range(len(graph))}
for i in data:
    print(dic[i], end=' ')