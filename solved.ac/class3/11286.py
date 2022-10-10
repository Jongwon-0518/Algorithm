from sys import stdin
import heapq

N = int(stdin.readline())
answer = []
for _ in range(N):
    x = int(stdin.readline())
    if x!= 0:
        heapq.heappush(answer, [abs(x), x])
    else:
        if answer:
            t = heapq.heappop(answer)
            print(t[1])
        else:
            print(0)