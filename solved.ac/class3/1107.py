import sys

N = int(sys.stdin.readline().rstrip())
ans = abs(100-N)
M = int(sys.stdin.readline().rstrip())
if M:
    broken = set(sys.stdin.readline().split())
else:
    broken = set()

for num in range(1000001):
    for i in str(num):
        if i in broken:
            break 5
    else:
        ans = min(ans, len(str(num))+abs(num-N))
    
print(ans) 