a, b = input().split()
N = int(a)
K = int(b)
c = []
s = 0
for i in range(N):
    c.append(int(input()))
if c[N-1] <= K:
    for i in range(N):
        s += K // c[N-1-i]
        K = K % c[N-i-1]
else:
    for k in range(N):
        if c[N-k-1] > K >= c[N-2-k]:
            for i in range(N-1-k):
                s += K // c[N-2-i-k]
                K = K % c[N-2-i-k]

print(s)