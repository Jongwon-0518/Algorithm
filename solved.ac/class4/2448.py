from sys import stdin
import math

N = int(stdin.readline())

unit = ["  *  ", " * * ", "*****"]

t = int(math.log2(N//3))

while t>0:
    x = len(unit)
    next = []
    for i in range(x):
        a = " "*x + unit[i] + " "*x
        next.append(a)
    for i in range(x):
        a = unit[i]+" "+unit[i]
        next.append(a)
        
    unit = next

    t -= 1

for i in range(len(unit)):
    print(unit[i])