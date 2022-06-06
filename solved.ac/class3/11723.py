import sys

N = sys.stdin.readline().rstrip()
S=set()
for _ in range(int(N)):
    word = sys.stdin.readline().strip().split()
    if len(word)==1:
        if word[0]=='all':
            S=set([i for i in range(1, 21)])
        elif word[0]=='empty':
            S=set()
    else:
        a, b = word[0], word[1]
        if a=='add': 
            S.add(int(b))
        elif a=='remove':
            S.discard(int(b))
        elif a=='check':
            print(1 if int(b) in S else 0)
        elif a=='toggle':
            if int(b) in S:
                S.discard(int(b))
            else:
                S.add(int(b))