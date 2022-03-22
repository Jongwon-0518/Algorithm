from sys import stdin

read = stdin.readline
ans = []
for i in range(int(read().rstrip('\n'))):
    cnt = 1
    data = []
    for i in range(int(read().rstrip('\n'))):
        data.append(list(map(int, read().split())))
    data.sort()
    max = data[0][1]
    for i in range(1, len(data)):
        if max > data[i][1]:
            cnt += 1
            max = data[i][1]
    ans.append(cnt)
    

for i in ans:
    print(i, end=('\n'))