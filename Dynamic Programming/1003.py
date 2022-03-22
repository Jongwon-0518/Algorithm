from sys import stdin

T = int(stdin.readline().rstrip('\n'))

# def fibonacci(n):
#     global a, b
#     if n==0:
#         a += 1
#         return 0
#     elif n==1:
#         b += 1
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# for _ in range(T):
#     i = int(stdin.readline().rstrip('\n'))
#     a, b = 0, 0
#     fibonacci(i)
#     print(a, b)

zero = [1, 0, 1]
one = [0, 1, 1]

def cal(num):
    l = len(zero)
    if l <= num:
        for i in range(l, num+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[num], one[num])

for _ in range(T):
    i = int(stdin.readline().rstrip('\n'))
    cal(i)