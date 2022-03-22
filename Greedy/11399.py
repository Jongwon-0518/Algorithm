# 사람의 수: N
N = int(input())
# 인출하는데 걸리는 시간: p
p = input().split()
for i in range(N):
    p[i] = int(p[i])
# 오름차순 정리
p.sort()
s = 0
# 돈을 인출하는데 필요한 시간의 합의 최솟값
for i in range(N):
    s += p[i] * (N-i)

print(s)

