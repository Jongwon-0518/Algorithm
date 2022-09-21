def solution(info, edges):
    global answer
    answer = 0
    node_n = len(info)
    data = [[] for _ in range(node_n)]
    for i in edges:
        data[i[0]].append(i[1])
        
    def dfs(node, lamb, wolf, canvisit):
        global answer
        if info[node]==0:
            lamb += 1
        elif info[node]==1:
            wolf += 1
        if lamb>answer:
            answer = lamb
        elif lamb<=wolf:
            return
        for i in canvisit:
            visit = canvisit.copy()     # 리스트 복제 이거루!! list.copy()
            visit.remove(i)
            visit += data[i]
            dfs(i, lamb, wolf, visit)

    dfs(0, 0, 0, data[0])
            
    return answer

info = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]
print(solution(info, edges))
