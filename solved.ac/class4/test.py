def solution(p):
    answer = ''
    i, a = 0, 0
    while i<len(p):
        if p[i]=='(':   a+=1
        else:   a-=1
        if a<0:
            break
        i+=1
    if a==0:
        answer = p
    else:
        if not p:
            answer = p
        u, v = [], []
        i, a = 0, 0
        while True:
            if p[i]=='(':   a+=1
            else:   a-=1
            u.append(p[i])
            i+=1
            if a==0:
                break
        for j in range(i, len(p)):
            v.append(p[i])
        answer = v
        
        
    return answer

print(solution(")("	))

def function(p):
    if not p:
        return p
    i, a = 0, 0
    u, v = [], []
    while True:
        if p[i]=='(':   a+=1
        else:   a-=1
        u.append(p[i])
        i+=1
        if a==0:
            break
    for j in range(i, len(p)):
        v.append(p[i])
    