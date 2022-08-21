from collections import deque

def trap(road_dic, x, n):
    new_road_dic = [[] for _ in range(n+1)]
    for p in range(n+1):
        if road_dic[p]:
            for q, s in road_dic[p]:
                if q==x or p==x:
                    new_road_dic[q].append((p, s))
                else:
                    new_road_dic[p].append((q, s))
    return new_road_dic

def solution(n, start, end, roads, traps):
    answer = []
    road_dic = [[] for _ in range(n+1)]
    
    for p, q, s in roads:
        road_dic[p].append((q, s))

    queue = deque([(start, 0, road_dic)])
    while queue:
        x, y, z = queue.popleft()
        
        if not answer or (answer and min(answer)>y):
            if x == end:
                answer.append(y)
            elif x in traps:
                road_dic = trap(z, x, n)
                for i in road_dic[x]:
                    queue.append((i[0], i[1]+y, road_dic))
            else:
                road_dic = z
                for i in road_dic[x]:
                    queue.append((i[0], i[1]+y, road_dic))
    
    return answer

print(solution(5, 1, 5, [[1, 2, 1], [2, 1, 1], [2, 3, 1], [3, 2, 1], [3, 5, 1]], [4]))