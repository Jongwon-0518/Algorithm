import sys
sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline().rstrip('\n'))
data = []
for _ in range(N):
    data.append(list(sys.stdin.readline().rstrip('\n')))

visited = [[False] * N for _ in range(N)]

three_cnt, two_cnt = 0, 0
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    #현재 색상 좌표를 방문해준다.
    visited[x][y] = True
    current_color = data[x][y]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if (0 <= nx < N) and (0 <= ny < N):
            #현재 좌표의 색상과 상하좌우 좌표에 있는 색상이 같으면 dfs로 넣어준다.
            if visited[nx][ny]==False:
                if data[nx][ny] == current_color:
                    dfs(nx,ny)

for i in range(N):
    for j in range(N):
        # 방문하지 않은 좌표이면 dfs로 넣어준다.
        if visited[i][j]==False:
            dfs(i,j)
            three_cnt += 1

#R을 G로 바꾸어준다. --> 적록색약은 같은 색으로 보기 때문에
for i in range(N):
    for j in range(N):
        if data[i][j]=='R':
            data[i][j]='G'

visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            dfs(i,j)
            two_cnt += 1

print(three_cnt,two_cnt)