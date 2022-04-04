import sys
sys.setrecursionlimit(10**6)
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def dfs(x, y):  #(x, y)에서 시작했을때 가능한 가짓수를 출력하는 함수
    if x == N-1 and y == M-1:   #도착시
        return 1
    if dp[x][y] != -1:  #이미 방문했으면
        return dp[x][y]
    dp[x][y] = 0    #방문안됬으면 방문한거니까 -1이 0으로
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:     #범위내에서
            if data[nx][ny] < data[x][y]:   #내리막길인 경우에만
                dp[x][y] += dfs(nx, ny)     #dp에 경로 가짓수 더해짐
    return dp[x][y]

N, M = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[-1]*M for _ in range(N)]
print(dfs(0, 0))

#print(dp) # 이거 출력해보면 원리 이해됨
