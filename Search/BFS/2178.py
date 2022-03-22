from sys import stdin

# readline이 input보다 효율적
n, m = map(int, stdin.readline().split())
# matrix 배열
matrix = [stdin.readline().rstrip() for _ in range(n)]
# 방문경로 배열
visited = [[0]*m for _ in range(n)]
# 좌/우/위/아래 방향 이동 
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# BFS 경로 탐색
# queue 방식
queue = [(0, 0)] #시작점
visited[0][0] = 1

while queue:
    x, y = queue.pop(0)
    
    if x == n-1 and y == m-1:
        # 최종 경로 도착
        print(visited[x][y])
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <n and 0 <= ny < m:
            if visited[nx][ny] == 0 and matrix[nx][ny] == '1':
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))