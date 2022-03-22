from sys import stdin

N = int(stdin.readline().rstrip('\n'))
a = []
b = []
sum = 0
for _ in range(N):
    i = int(stdin.readline().rstrip('\n'))
    if i>0:
        a.append(i)
    else:
        b.append(i)
a.sort(reverse=True)
b.sort()
if len(a)%2==0:
    for i in range(0, len(a), 2):
        if a[i]==1 or a[i+1]==1:
            sum += a[i]
            sum += a[i+1]
        else:
            sum += a[i]*a[i+1]
else:
    for i in range(0, len(a)-1, 2):
        if a[i]==1 or a[i+1]==1:
            sum += a[i]
            sum += a[i+1]
        else:
            sum += a[i]*a[i+1]
    sum += a[-1]
if len(b)%2==0:
    for i in range(0, len(b), 2):
        sum += b[i]*b[i+1]
else:
    for i in range(0, len(b)-1, 2):
        sum += b[i]*b[i+1]
    sum += b[-1]
print(sum)