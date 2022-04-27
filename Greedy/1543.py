import sys

data = sys.stdin.readline().rstrip()
ans = sys.stdin.readline().rstrip()
cnt = 0
i=0
while i < len(data)-len(ans)+1:
    if data[i:i+len(ans)] == ans:
        cnt +=1
        i = i-1+len(ans)
    i += 1

print(cnt)