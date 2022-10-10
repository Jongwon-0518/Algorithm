def solution(alp, cop, problems):
    max_alp, max_cop = 0, 0
    for i in problems:
        max_alp = max(max_alp, i[0])
        max_cop = max(max_cop, i[1])

    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    INF = float('inf')
    dp = [[INF]*(max_cop+1) for _ in range(max_alp+1)]
    dp[alp][cop] = 0

    for i in range(alp, max_alp+1):
        for j in range(cop, max_cop+1):
            if i+1<=max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            if j+1<=max_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            for alp_req, cop_req, alp_rew, cop_rew, cost in problems:
                if i >= alp_req and j >= cop_req:
                    next_alp, next_cop = min(max_alp, i+alp_rew), min(max_cop, j+cop_rew)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j]+cost)
                

    for i in range(len(dp)):
        print(dp[i])
    return dp[-1][-1]

alp = 0
cop = 0
problems = [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]
print(solution(alp, cop, problems))