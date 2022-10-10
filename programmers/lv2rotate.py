def rotate(query, graph):
    x1, y1, x2, y2 = query[0]-1, query[1]-1, query[2]-1, query[3]-1
    next_graph = [i[:] for i in graph] ## 슬라이싱을 이용한 깊이복사
    total = []
    for i in range(y1, y2):
        next_graph[x1][i+1] = graph[x1][i]
        next_graph[x2][i] = graph[x2][i+1]
        total.append(next_graph[x1][i+1])
        total.append(next_graph[x2][i])
    for i in range(x1, x2):
        next_graph[i][y1] = graph[i+1][y1]
        next_graph[i+1][y2] = graph[i][y2]
        total.append(next_graph[i][y1])
        total.append(next_graph[i+1][y2])

    return next_graph, min(total)

def solution(rows, columns, queries):
    answer = []
    graph = [list(range(i*columns+1, i*columns+columns+1)) for i in range(rows)]
    for i in queries:
        graph, x = rotate(i, graph)
        answer.append(x)
    return answer

print(solution(6, 8, []))

## 깊이복사 deepcopy는 시간 너무 잡아먹음 쓰지말것
## 슬라이싱 쓸것