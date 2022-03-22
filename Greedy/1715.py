from sys import stdin
import heapq

n = int(stdin.readline().rstrip('\n'))
data = []
for _ in range(n):
    data.append(int(stdin.readline().rstrip('\n')))
heapq.heapify(data)
ans = 0

while len(data) != 1:
    num1 = heapq.heappop(data)
    num2 = heapq.heappop(data)
    sum = num1 + num2
    ans += sum
    heapq.heappush(data, sum)

print(ans)