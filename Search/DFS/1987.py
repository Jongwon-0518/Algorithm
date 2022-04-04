r, c = list(map(int, input().split()))

board = []
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for _ in range(r):
    board.append(input())

visited = [False for _ in range(26)]
DIFF = ord('A')
def dfs(x, y):
    global visited

    asc = ord(board[x][y])
    visited[asc-DIFF] = True
    cnt = 1

    local_max_cnt = 0
    for dx, dy in dxy:
        if x+dx < 0 or x+dx >= r or y+dy < 0 or y+dy >= c:
            continue
        _asc = ord(board[x+dx][y+dy])
        if not visited[_asc-DIFF]:
            visited[_asc-DIFF] = True
            local_cnt = dfs(x+dx, y+dy)
            local_max_cnt = local_cnt if local_cnt > local_max_cnt else local_max_cnt
            visited[_asc-DIFF] = False

    cnt += local_max_cnt
    return cnt

print(dfs(0, 0))