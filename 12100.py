from sys import stdin

def moveL(data):
    N = len(data)
    new_data = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        dp = []
        for j in range(N):
            if data[i][j] != 0:
                if not dp:
                    dp.append(data[i][j])
                    K = True
                else:
                    if dp[-1] == data[i][j] and K:
                        dp[-1] *= 2
                        K = False
                    else:
                        dp.append(data[i][j])
                        K = True
        if dp:
            for j in range(len(dp)):
                new_data[i][j] = dp[j]
    return new_data

def moveR(data):
    N = len(data)
    new_data = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        dp = []
        for j in range(N-1, -1, -1):
            if data[i][j] != 0:
                if not dp:
                    dp.append(data[i][j])
                    K = True
                else:
                    if dp[-1] == data[i][j] and K:
                        dp[-1] *= 2
                        K = False
                    else:
                        dp.append(data[i][j])
                        K = True
        if dp:
            for j in range(len(dp)):
                new_data[i][N-1-j] = dp[j]
    return new_data

def moveU(data):
    N = len(data)
    new_data = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        dp = []
        for j in range(N):
            if data[j][i] != 0:
                if not dp:
                    dp.append(data[j][i])
                    K = True
                else:
                    if dp[-1] == data[j][i] and K:
                        dp[-1] *= 2
                        K = False
                    else:
                        dp.append(data[j][i])
                        K = True
        if dp:
            for j in range(len(dp)):
                new_data[j][i] = dp[j]
    return new_data

def moveD(data):
    N = len(data)
    new_data = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        dp = []
        for j in range(N-1, -1, -1):
            if data[j][i] != 0:
                if not dp:
                    dp.append(data[j][i])
                    K = True
                else:
                    if dp[-1] == data[j][i] and K:
                        dp[-1] *= 2
                        K = False
                    else:
                        dp.append(data[j][i])
                        K = True
        if dp:
            for j in range(len(dp)):
                new_data[N-1-j][i] = dp[j]
    return new_data

def function(data, k):
    if k==5:
        matrix = []
        for i in range(len(data)):
            matrix.append(max(data[i]))
        answer.append(max(matrix))
    else:
        for i in range(4):
            if i==0:
                new_data = moveD(data)
                function(new_data, k+1)
            elif i==1:
                new_data = moveU(data)
                function(new_data, k+1)
            elif i==2:
                new_data = moveR(data)
                function(new_data, k+1)
            elif i==3:
                new_data = moveL(data)
                function(new_data, k+1)



N = int(stdin.readline())
data = []
for _ in range(N):
    data.append(list(map(int, stdin.readline().split())))
answer = []
function(data, 0)
print(max(answer))