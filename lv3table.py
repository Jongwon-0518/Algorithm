from collections import deque

def solution(n, k, cmd):
    answer = ''
    n_list = list(range(n))
    trash = deque([])
    for i in cmd:
        if i[0]=='D':
            k += int(i[2])
        elif i[0]=='U':
            k -= int(i[2])
        elif i[0]=="C":
            if k==len(n_list):
                trash.append((k, n_list[k]))
                del n_list[k]
                k -= 1
            else:
                trash.append((k, n_list[k]))
                del n_list[k]  
        elif i[0]=='Z':
            x, name = trash.pop()
            n_list = n_list[:x] + [name] + n_list[x:]
            if x<k:
                k+=1
    for i in range(n):
        if i in n_list:
            answer += 'O'
        else:
            answer += 'X'
    print(n_list)
    return answer

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]	
print(solution(n, k, cmd))