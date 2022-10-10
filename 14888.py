from sys import stdin

N = int(stdin.readline())
data = list(map(int, stdin.readline().split()))
cal = list(map(int, stdin.readline().split()))
answer = []

def dfs(ans, j, cal):
    if j == len(data):
        answer.append(ans)
        return
    for i in range(4):
        if i==0 and cal[i]>0:
            new_ans = ans + data[j]
            new_cal = cal[:]
            new_cal[i] -= 1
            dfs(new_ans, j+1, new_cal)
        elif i==1 and cal[i]>0:
            new_ans = ans - data[j]
            new_cal = cal[:]
            new_cal[i] -= 1
            dfs(new_ans, j+1, new_cal)
        elif i==2 and cal[i]>0:
            new_ans = ans * data[j]
            new_cal = cal[:]
            new_cal[i] -= 1
            dfs(new_ans, j+1, new_cal)
        elif i==3 and cal[i]>0:
            if ans<0:
                new_ans = (abs(ans) // data[j])*(-1)
            elif ans>=0:
                new_ans = ans // data[j]
            new_cal = cal[:]
            new_cal[i] -= 1
            dfs(new_ans, j+1, new_cal)

dfs(data[0], 1, cal)

print(max(answer))
print(min(answer))