from itertools import product

def match(id1, id2):
    id1_n = len(id1)
    id2_n = len(id2)
    i = 0
    correct = True
    if id1_n != id2_n:
        return False
    elif id1_n == id2_n:
        if id1 == '*'*id1_n:
            return True
        while i<id1_n:
            if id1[i]==id2[i] or id1[i]=='*':
                i += 1
            else:
                correct = False
                break
        return correct

def solution(user_id, banned_id):
    banned = []
    k = len(banned_id)
    
    for i in banned_id:
        banned.append([])
        for j in user_id:
            if match(i, j):
                banned[-1].append(j)

    answer = list(product(*banned))
    print(answer)
    answer_new = []

    for i in range(len(answer)):
        a = set(answer[i])
        if len(a) == k:
            if a not in answer_new:
                answer_new.append(a)

    return answer_new


user_id =  	["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id =   ["fr*d*", "abc1**"]
print(solution(user_id, banned_id))