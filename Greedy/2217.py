n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

a.sort()

k = -1
for i in range(n):
    j = a[i] * (n - i)
    k = max(j, k)

print(k)