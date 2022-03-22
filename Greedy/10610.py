from sys import stdin

nums = list(map(int, stdin.readline().rstrip('\n')))
nums.sort(reverse=True)
sum=0
for i in nums:
    sum += i
if nums[-1]==0 and sum%3==0:
    for i in nums:
        print(i, end='')
else:
    print(-1)