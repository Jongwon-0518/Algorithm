from sys import stdin

N = int(stdin.readline().rstrip('\n'))
data = []
for _ in range(N):
    data.append(list(map(int, stdin.readline().split())))
data.append([0, 0, 0])

for i in range(1, N):
    data[i][0] = min(data[i-1][1], data[i-1][2]) + data[i][0]
    data[i][1] = min(data[i-1][0], data[i-1][2]) + data[i][1]
    data[i][2] = min(data[i-1][0], data[i-1][1]) + data[i][2]

print(min(data[N-1]))