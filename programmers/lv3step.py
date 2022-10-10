import copy

def solution(board, aloc, bloc):
    answer = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    N = len(board)
    M = len(board[0])

    def dfsA(a, b, graph, control, cnt):
        graph_new = copy.deepcopy(graph)

        if control == 0:
            if a==b:
                answer.append(cnt+1)
                return
            graph_new[a[0]][a[1]] = 0
            na = []
            p = 0
            for i in range(4):
                na.append([a[0]+dx[i], a[1]+dy[i]])
            di = {}
            di1 = {}
            for i in range(4):
                if 0<=na[i][0]<N and 0<=na[i][1]<M:
                    if graph_new[na[i][0]][na[i][1]] == 1:
                        di[i] = na[i]
                        di1[i] = abs(di[i][0]-b[0]) + abs(di[i][1]-b[1])
                    else:
                        p += 1
                else:
                    p += 1
            if p == 4:
                answer.append(cnt)
                return
            di1 = sorted(di1.items(), key=lambda x:x[1])
            
            cnt += 1
            for i in range(len(di1)):
                if i>0 and di1[i][1]!=di1[i-1][1]:
                    break
                print([di[di1[i][0]][0], di[di1[i][0]][1]], b, graph_new, 1, cnt)
                dfsA([di[di1[i][0]][0], di[di1[i][0]][1]], b, graph_new, 1, cnt)
        
        elif control == 1:
            if a==b:
                answer.append(cnt+1)
                return
            graph_new[b[0]][b[1]] = 0
            nb = []
            p = 0
            for i in range(4):
                nb.append([b[0]+dx[i], b[1]+dy[i]])
            di = {}
            di1 = {}
            for i in range(4):
                if 0<=nb[i][0]<N and 0<=nb[i][1]<M:
                    if graph_new[nb[i][0]][nb[i][1]] == 1:
                        di[i] = nb[i]
                        di1[i] = abs(di[i][0]-a[0]) + abs(di[i][1]-a[1])
                    else:
                        p += 1
                else:
                    p += 1
            if p == 4:
                answer.append(cnt)
                return
            di1 = sorted(di1.items(), key=lambda x:x[1], reverse=True)
            cnt += 1
            for i in range(len(di1)):
                if i>0 and di1[i][1]!=di1[i-1][1]:
                    break
                print(a, [di[di1[i][0]][0], di[di1[i][0]][1]], graph_new, 0, cnt)
                dfsA(a, [di[di1[i][0]][0], di[di1[i][0]][1]], graph_new, 0, cnt)

    def dfsB(a, b, graph, control, cnt):
        graph_new = copy.deepcopy(graph)

        if control == 0:
            if a==b:
                answer.append(cnt)
                return
            graph_new[a[0]][a[1]] = 0
            na = []
            p = 0
            for i in range(4):
                na.append([a[0]+dx[i], a[1]+dy[i]])
            di = {}
            di1 = {}
            for i in range(4):
                if 0<=na[i][0]<N and 0<=na[i][1]<M:
                    if graph_new[na[i][0]][na[i][1]] == 1:
                        di[i] = na[i]
                        di1[i] = abs(di[i][0]-b[0]) + abs(di[i][1]-b[1])
                    else:
                        p += 1
                else:
                    p += 1
            if p == 4:
                answer.append(cnt)
                return
            di1 = sorted(di1.items(), key=lambda x:x[1], reverse=True)
            cnt += 1
            for i in range(len(di1)):
                if i>0 and di1[i][1]!=di1[i-1][1]:
                    break
                dfsB([di[di1[i][0]][0], di[di1[i][0]][1]], b, graph_new, 1, cnt)
        
        elif control == 1:
            if a==b:
                answer.append(cnt+1)
                return
            graph_new[b[0]][b[1]] = 0
            nb = []
            p = 0
            for i in range(4):
                nb.append([b[0]+dx[i], b[1]+dy[i]])
            di = {}
            di1 = {}
            for i in range(4):
                if 0<=nb[i][0]<N and 0<=nb[i][1]<M:
                    if graph_new[nb[i][0]][nb[i][1]] == 1:
                        di[i] = nb[i]
                        di1[i] = abs(di[i][0]-a[0]) + abs(di[i][1]-a[1])
                    else:
                        p += 1
                else:
                    p += 1
            if p == 4:
                answer.append(cnt)
                return
            di1 = sorted(di1.items(), key=lambda x:x[1])
            cnt += 1
            for i in range(len(di1)):
                if i>0 and di1[i][1]!=di1[i-1][1]:
                    break
                dfsB(a, [di[di1[i][0]][0], di[di1[i][0]][1]], graph_new, 0, cnt)

    
    dfsA(aloc, bloc, board, 0, 0)
    dfsB(aloc, bloc, board, 0, 0)

    return min(answer)

board = 	[[1, 1, 1], [1, 1, 1], [1, 1, 1]]
aloc = [1, 0]
bloc = [1, 2]	
print(solution(board, aloc, bloc))