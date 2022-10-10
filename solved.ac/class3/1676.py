from sys import stdin

N = int(stdin.readline())

answer, i = 1, 1

while i<=N:
    answer *= i
    i += 1

answer = str(answer)
res = 0
for j in range(len(answer)-1, -1, -1):
    if answer[j]=='0':
        res += 1
    else:
        break

print(res)