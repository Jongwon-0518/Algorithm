from sys import stdin

T = int(stdin.readline().rstrip('\n'))

def cal(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        return  cal(n-1) + cal(n-2) + cal(n-3)

for i in range(T):
    n = int(stdin.readline().rstrip('\n'))
    print(cal(n))