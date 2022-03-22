from sys import stdin

i = 1

while True:
    L, P, V = map(int, stdin.readline().split())
    if L == 0 and P == 0 and V == 0:
        break
    if V%P>L:
        res = (V//P)*L+L
    else:
        res = (V//P)*L+V%P
    print("Case %d: %d" %(i, res))
    i += 1