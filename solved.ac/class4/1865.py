from sys import stdin
import sys

TC = int(stdin.readline())

INF = sys.maxsize

# 밸만포드 - 음의 순환 확인 가능
def bellman_ford():
    distance = [INF]*(N+1)
    for i in range(N):
        for j in range(len(edges)):
            node = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]

            if distance[next_node] > distance[node]+cost:
                distance[next_node] = distance[node]+cost

                if i==N-1:  # 음의 순환 확인
                    return False
    return True

for _ in range(TC):
    N, M, W = map(int, stdin.readline().split())
    edges = []
    for _ in range(M):
        S, E, T = map(int, stdin.readline().split())
        edges.append((S, E, T))
        edges.append((E, S, T))

    for _ in range(W):
        S, E, T = map(int, stdin.readline().split())
        edges.append((S, E, -T))

    answer = bellman_ford()

    if answer:
        print('NO')
    else:
        print("YES")
