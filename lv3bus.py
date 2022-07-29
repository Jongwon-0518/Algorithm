from collections import deque
def solution(n, t, m, timetable):
    timetables = []
    bus = [[] for _ in range(n)]
    for i in timetable:
        a, b = map(int, i.split(':'))
        timetables.append(60*a+b)
    timetables.sort()
    timetables = deque(timetables)
    j = 0
    for i in range(540, n*t+540, t):
        if j>=n:
            break
        for _ in range(m):
            if timetables:
                x = timetables.popleft()
                if x>i:
                    timetables.appendleft(x)
                    break
                else:
                    bus[j].append(x)
        j+=1
    if not bus[-1]:
        answer = answer = (n-1)*t+540
    elif len(bus[-1])<m:
        answer = (n-1)*t+540
    elif len(bus[-1])==m:
        answer = bus[-1][-1]-1
    if answer == 1440:
        answer = 1439
    
    answer = str(answer//60).zfill(2) + ":" + str(answer%60).zfill(2)

    return answer

n = 3
t = 1
m = 2
timetable = [ "06:00", "23:59", "05:48", "00:01", "00:01"]
print(solution(n, t, m, timetable))