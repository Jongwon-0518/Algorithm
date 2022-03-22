from sys import stdin

sum = 0
i = 1
s = int(stdin.readline().rstrip('\n'))

while True:
    s -= i
    i += 1
    sum += 1
    if s < i:
        break

print(sum)