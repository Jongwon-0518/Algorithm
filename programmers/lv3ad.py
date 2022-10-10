### 누적합으로 누적시청자수를 구해서 품


def strtotime(a):
    h, m, s = map(int, a.split(':'))
    return h*60*60+m*60+s

def timetostr(a):
    h = a//3600
    m = (a%3600)//60
    s = a-h*3600-m*60
    h, m, s = str(h), str(m), str(s)
    answer = h.zfill(2)+":"+m.zfill(2)+":"+s.zfill(2)
    return answer



def solution(play_time, adv_time, logs):
    play_time = strtotime(play_time)
    adv_time = strtotime(adv_time)
    all_time = [0]*(play_time+1)
    
    for i in logs:
        start, end = i.split("-")
        all_time[strtotime(start)] += 1
        all_time[strtotime(end)] -= 1
    
    for i in range(1, play_time+1):
        all_time[i] += all_time[i-1]
    
    for i in range(1, play_time+1):
        all_time[i] += all_time[i-1]

    most_view, max_time = 0, 0

    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < all_time[i] - all_time[i - adv_time]:
                most_view = all_time[i] - all_time[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if most_view < all_time[i]:
                most_view = all_time[i]
                max_time = i - adv_time + 1

    return timetostr(max_time)

print(solution("02:03:55"	, "00:14:15"	, ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]	))