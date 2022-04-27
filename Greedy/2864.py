import sys

A, B = sys.stdin.readline().split()

A1 = A.replace("6", "5")
B1 = B.replace("6", "5")
min = int(A1)+int(B1)
A2 = A.replace("5", "6")
B2 = B.replace("5", "6")
max = int(A2)+int(B2)

print(min, max)
