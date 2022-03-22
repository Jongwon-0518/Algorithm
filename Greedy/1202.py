# from operator import itemgetter
# from sys import stdin

# N, K = map(int, stdin.readline().split())
# data = []
# bag = []
# res = 0
# matrix = [0]*(K)

# for _ in range(N):
#     data.append(list(map(int, stdin.readline().split())))

# data.sort(key=itemgetter(1), reverse=True)

# for _ in range(K):
#     bag.append(int(stdin.readline().rstrip('\n')))

# bag.sort()

# for i in range(N):
#     j = 0
#     while j < K:
#         if matrix[j] == 0 and bag[j] >= data[i][0]:
#             matrix[j] = 1
#             res += data[i][1]
#             break
#         j += 1

# print(res)

import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
jew = []
for _ in range(N):
    heapq.heappush(jew, list(map(int, sys.stdin.readline().split())))
bags = []
for _ in range(K):
    bags.append(int(sys.stdin.readline()))
bags.sort()

answer = 0
tmp_jew = []
for bag in bags:
    while jew and bag >= jew[0][0]:
        heapq.heappush(tmp_jew, -heapq.heappop(jew)[1])
    if tmp_jew:
        answer -= heapq.heappop(tmp_jew)
    elif not jew:
        break
print(answer)