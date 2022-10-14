from sys import stdin

n = int(stdin.readline())

answer = [0, 1, 3, 5]

for i in range(n+1):
    if i>3:
        answer.append(answer[i-2]*2+answer[i-1])

print(answer[n]%10007)