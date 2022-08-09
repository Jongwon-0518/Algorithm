# 플로이드 워셜 알고리즘

def solution(n, s, x, y, fares):
    INF = int(1e9)    # 간선의 개수

    # 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for a in range(1, n + 1):
        graph[a][a] = 0
    
    # 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
    for c, d, f in fares:
        graph[c][d] = graph[d][c] = f

    # 점화식에 따라 플로이드 워셜 알고리즘을 수행
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    answer = []

    for i in range(1, n+1):
        answer.append(graph[s][i] + graph[i][x] + graph[i][y])
    return min(answer)

n = 7
s = 3
x = 4
y = 1
fares = 	[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
print(solution(n, s, x, y, fares))
