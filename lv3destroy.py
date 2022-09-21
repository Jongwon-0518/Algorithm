# 정확성만 통과 브루트포스
def solution1(board, skill):
    answer = 0
    
    def attack(a):
        for i in range(a[1], a[3]+1):
            for j in range(a[2], a[4]+1):
                board[i][j] -= a[5]
    
    def hill(a):
        for i in range(a[1], a[3]+1):
            for j in range(a[2], a[4]+1):
                board[i][j] += a[5]
    
    for i in skill:
        if i[0]==1:
            attack(i)
        elif i[0]==2:
            hill(i)
    
    for i in board:
        for j in i:
            if j>0:
                answer += 1

    return answer

# 효율성도 통과 누적합
def solution2(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])
    x = [[0 for _ in range(M+1)] for _ in range(N+1)]
    
    for i in skill:
        if i[0]==1:
            x[i[1]][i[2]] -= i[5]
            x[i[1]][i[4]+1] += i[5]
            x[i[3]+1][i[2]] += i[5]
            x[i[3]+1][i[4]+1] -= i[5]
        elif i[0]==2:
            x[i[1]][i[2]] += i[5]
            x[i[1]][i[4]+1] -= i[5]
            x[i[3]+1][i[2]] -= i[5]
            x[i[3]+1][i[4]+1] += i[5]

    for i in range(M):
        for j in range(N-1):
            x[j+1][i] += x[j][i]

    for i in range(N):
        for j in range(M-1):
            x[i][j+1] += x[i][j]

    for i in range(N):
        for j in range(M):
            board[i][j] += x[i][j]
            if board[i][j]>0:
                answer += 1

    return answer

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]	
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]	
print(solution1(board, skill))

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]	
print(solution2(board, skill))