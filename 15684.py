from sys import stdin

N, M, H = map(int, stdin.readline().split())
line = []
if M == 0:
    print(0)
elif M > 0:
    for i in range(M):
        line.append(list(map(int, stdin.readline().split())))
    matrix = [[0 for _ in range(N-1)] for _ in range(M)]
    for i in line:
        matrix[i[0]-1][i[1]-1] = 1
    
print(matrix)