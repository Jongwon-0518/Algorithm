import sys

n = int(sys.stdin.readline().rstrip())
dp = [1, 3]
for i in range(2, n):
    if i%2==0:
        dp.append(dp[i-1]*2-1)
    else:
        dp.append(dp[i-1]*2-1+2*dp[i-2])
print(dp)