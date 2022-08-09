def moveL(data):
    N = len(data)
    for i in range(N):
        dp = [(i, 0, data[i][0])]
        for j in range(1, N):
            if data[i][j] != 0:
                if data[i][j] == dp[-1][2]:
                    data[dp[-1][0]][dp[-1][1]] *= 2
                    
