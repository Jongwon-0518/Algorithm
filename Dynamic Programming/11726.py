from sys import stdin

n = int(stdin.readline().rstrip('\n'))

if n == 1:
    print(1)
elif n==2:
    print(2)
else:
    data = [0]*n
    data[0] = 1
    data[1] = 2
    for i in range(2, n):
        data[i] = data[i-1] + data[i-2]
    print(data[n-1]%10007)
