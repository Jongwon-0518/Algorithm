n = int(input())
y = []

for i in range(n):
  x = list(map(int, input().split()))
  y.append(x)
y.sort(key = lambda a:a[0])
y.sort(key = lambda a:a[1])

resent = -1
cnt = 0
for i in range(n):
  if y[i][0] >= resent:
    resent = y[i][1]
    cnt += 1

print(cnt)