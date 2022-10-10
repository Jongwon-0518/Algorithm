from sys import stdin
from collections import deque

T = int(stdin.readline())

for _ in range(T):
    p = stdin.readline()
    n = int(stdin.readline())
    data = stdin.readline().rstrip()[1:-1].split(',')
    queue = deque(data)

    rev= 0
    flag = 0
    
    if n==0:
        queue = []

    for j in p:
        if j=='R':
            rev+=1
        elif j=='D':
            if len(queue)<1:
                flag = 1
                print("error")
                break
            else:
                if rev%2==0:
                    queue.popleft()
                else:
                    queue.pop()
    
    if flag==0:
        if rev%2==0:
            print("["+",".join(queue)+"]")
        else:
            queue.reverse()
            print("["+",".join(queue)+"]")