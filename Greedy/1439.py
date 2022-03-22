from sys import stdin

s = stdin.readline().rstrip('\n')
m, a = 0, 0
for i in s:
    if a != int(i):
        m += 1
    a = int(i)

if int(s[0]) == 1:
    m -= 1

if m%2 != 0:
    m = (m+1)//2
else:
    m = m//2

print(m)