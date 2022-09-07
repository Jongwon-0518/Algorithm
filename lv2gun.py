def function2(i, k, data, answer, answer_list):
        if len(answer)==11:
            answer_list.append(answer)
            return
        else:
            function2(i+1, k, data, answer + [0], answer_list)
            if data[i]+1<=k:
                function2(i+1, k-data[i]-1, data, answer + [data[i]+1], answer_list)


def solution(n, info):
    answer_list = []

    def score(a, b):
        a_score, b_score = 0, 0
        for i in range(11):
            if a[i] == b[i] == 0:
                pass
            elif a[i] < b[i]:
                b_score += (10-i)
            else:
                a_score += (10-i)
        return b_score - a_score

    
    function2(0, n, info, [], answer_list)

    new_answer_list = []

    for i in answer_list:
        if sum(i)<n:
            i[10] += (n-sum(i))
        new_answer_list.append([score(info, i), i])
    
    new_answer_list.sort()
    res = []
    for i in range(len(new_answer_list)-1, -1, -1):
        if new_answer_list[i][0] == new_answer_list[-1][0]:
            res.append(new_answer_list[i][1])
        else:
            break
    for i in res:
        i.reverse()
    res.sort()
    for i in res:
        i.reverse()
    if new_answer_list[-1][0] > 0:
        return res[-1]
    else:
        return [-1]

n = 9
info = [0,0,1,2,0,1,1,1,1,1,1]
print(solution(3, [0,0,1,0,0,0,0,0,0,1,0]))