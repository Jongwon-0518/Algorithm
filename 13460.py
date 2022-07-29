N, M = map(int, input().split())

data = []
answer = []
queue = []

for _ in range(N):
    data.append(list(input()))

visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

def posit():
    for x in range(N):
        for y in range(M):
            if data[x][y]=='R':
                Rx, Ry = x, y
            elif data[x][y]=='B':
                Bx, By = x, y
    queue.append((Rx, Ry, Bx, By, 1))
    visited[Rx][Ry][Bx][By] = True

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def move(x, y, dx, dy):
    cnt = 0  # 이동 칸 수
    # 다음이 벽이거나 현재가 구멍일 때까지
    while data[x+dx][y+dy] != '#' and data[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def solve():
    posit()  # 시작 조건
    while queue:  # BFS : queue 기준
        rx, ry, bx, by, depth = queue.pop(0)
        if depth > 10:  # 실패 조건
            break
        for i in range(4):  # 4방향 이동 시도
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])  # Red
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])  # Blue
            if data[nbx][nby] != 'O':  # 실패 조건이 아니면
                if data[nrx][nry] == 'O':  # 성공 조건
                    print(depth)
                    return
                if nrx == nbx and nry == nby:  # 겹쳤을 때
                    if rcnt > bcnt:  # 이동거리가 많은 것을
                        nrx -= dx[i]  # 한 칸 뒤로
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                # breadth 탐색 후, 탐사 여부 체크
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    # 다음 depth의 breadth 탐색 위한 queue
                    queue.append((nrx, nry, nbx, nby, depth+1))
    print(-1)  # 실패 시

solve()