import sys

N, M = map(int, sys.stdin.readline().split())

if N==1:
    print(1)
elif N==2:
    if M<=2:
        print(1)
    elif M<=4:
        print(2)
    elif M<=6:
        print(3)
    else:
        print(4)
else:
    if M<=4:
        print(M)
    elif M<=6:
        print(4)
    else:
        print(M-2)