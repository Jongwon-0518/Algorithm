from sys import stdin

N, M = map(int, stdin.readline().split())
a = stdin.readline().rstrip()
if a[0] == '0':
    real = set()
else:
    real = set(map(int, a[2:].split())) # 진실 말한사람

party = []

for _ in range(M):
    party.append(list(map(int, stdin.readline().split()))[1:])

k = [0]*60
uni = real.copy()

answer = 0
dp = [0]
for i in range(len(party)):
        pt = set(party[i])
        if pt&real:
            uni = uni | pt

dp = [k, uni]

while len(dp[-1])!=len(dp[-2]):
    newuni = set()
    for i in range(len(party)):
        pt = set(party[i])
        if pt&dp[-1]:
            newuni = newuni | pt
    dp.append(newuni)
    
    

for i in range(len(party)):
    pt = set(party[i])
    if pt&newuni:
        pass
    else:
        answer += 1

print(answer)