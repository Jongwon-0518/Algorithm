from sys import stdin

n = stdin.readline().rstrip('\n')
data = list(map(int, stdin.readline().split()))
sum = [data[0]]

for i in range(len(data)-1):
    sum.append(max(sum[i]+data[i+1], data[i+1]))

print(max(sum))