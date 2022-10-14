from sys import stdin

N, M = map(int, stdin.readline().split())
dic = {}
for _ in range(N):
    address, password = stdin.readline().split()
    dic[address] = password

for _ in range(M):
    address = stdin.readline().rstrip()
    print(dic[address])