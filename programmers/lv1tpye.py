def solution(survey, choices):
    answer = ''
    dic = {}
    str = 'RTCFJMAN'
    for i in str:
        dic[i] = 0
    N = len(choices)
    for i in range(N):
        score = choices[i]-4
        if score > 0:
            dic[survey[i][1]]+=score
        elif score < 0:
            dic[survey[i][0]]-=score

    if dic['R'] >= dic['T']:
        answer += 'R'
    else:
        answer += 'T'
    if dic['C'] >= dic['F']:
        answer += 'C'
    else:
        answer += 'F'
    if dic['J'] >= dic['M']:
        answer += 'J'
    else:
        answer += 'M'
    if dic['A'] >= dic['N']:
        answer += 'A'
    else:
        answer += 'N'
    return answer

survey = ["AN", "CF", "MJ", "RT", "NA"]	
choices = [5, 3, 2, 7, 5]
print(solution(survey, choices))