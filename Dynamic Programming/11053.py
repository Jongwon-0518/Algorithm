import sys
input = sys.stdin.readline

A = int(input().rstrip('\n'))
data = list(map(int, input().split()))
dp = [1]*A

for i in range(A):
    for j in range(i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))