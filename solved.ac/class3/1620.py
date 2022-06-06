import sys
N, M = map(int, sys.stdin.readline().split())
name = {}
for i in range(1, N+1):
    a = sys.stdin.readline().rstrip()
    name[i] = a
    name[a] = i
for _ in range(M):
    b = sys.stdin.readline().rstrip()
    if b.isdigit():
        print(name[int(b)])
    else:
        print(name[b])