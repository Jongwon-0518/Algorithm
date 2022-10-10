def solution(lottos, win_nums):

    correct = 0
    for i in lottos:
        if i in win_nums:
            correct += 1
    x = lottos.count(0)
    min = 7-correct
    if min>=6:
        min = 6
    max = 7-correct-x
    if max>=6:
        max = 6

    answer = [max, min]
    return answer