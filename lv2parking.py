def solution(fees, records):
    answer = []
    time = {}
    price = {}
    data = {}
    for i in records:
        i = list(i.split())
        if i[2] == "IN":
            data[i[1]] = int(i[0][:2])*60 + int(i[0][3:])
            if i[1] not in time:
                time[i[1]] = 0
        elif i[2] == "OUT":
            times = int(i[0][:2])*60 + int(i[0][3:]) - data[i[1]]
            time[i[1]] += times
            del(data[i[1]])

    if data:
        for key in data:
            times = 1439-data[key]
            time[key] += times

    for key in time:
        price[key] = 0
        if time[key] <= fees[0]:
            price[key] += fees[1]
        else:
            price[key] += fees[1] + ((time[key]-fees[0])//fees[2])*fees[3]
            if (time[key]-fees[0])%fees[2] > 0:
                price[key] += fees[3]

    price = sorted(price.items())

    for i in price:
        answer.append(i[1])

    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))