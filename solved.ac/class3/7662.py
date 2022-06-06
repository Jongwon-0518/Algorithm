import sys
import heapq

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    K = int(sys.stdin.readline().rstrip())
    Q1, Q2 = [], []
    visited = [False]*K
    for j in range(K):
        a, b = sys.stdin.readline().split()
        if a == 'I':
            heapq.heappush(Q1, (int(b), j))
            heapq.heappush(Q2, (-int(b), j))
            visited[j] = True
        else:
            if b == '1':
                while Q2 and not visited[Q2[0][1]]:
                    heapq.heappop(Q2)
                if Q2:
                    visited[Q2[0][1]] = False
                    heapq.heappop(Q2)
            else:
                while Q1 and not visited[Q1[0][1]]:
                    heapq.heappop(Q1)
                if Q1:
                    visited[Q1[0][1]] = False
                    heapq.heappop(Q1)
    
    while Q1 and not visited[Q1[0][1]]:
        heapq.heappop(Q1)
    while Q2 and not visited[Q2[0][1]]:
        heapq.heappop(Q2)
    
    if not Q1 or not Q2:
        print("EMPTY")
    else:
        a = -Q2[0][0]
        b = Q1[0][0]
        print("%d %d" % (a, b))