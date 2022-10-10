def solution(enroll, referral, seller, amount):
    answer = {}
    node_dic = {}
    seller_dic = {}
    seller_n = len(seller)
    enroll_n = len(enroll)
    for i in range(seller_n):
        seller_dic[i] = [seller[i], amount[i]*100]
    
    for i in range(enroll_n):
        node_dic[enroll[i]] = referral[i]
        answer[enroll[i]] = 0

    
    for i in range(seller_n):
        x = seller_dic[i][1]//10
        answer[seller_dic[i][0]] += seller_dic[i][1] - x
        dp = node_dic[seller_dic[i][0]]
        while dp != '-' and x != 0:
            answer[dp] += x - x//10
            x = x//10
            dp = node_dic[dp]

    result = list(answer.values())

    return result

print(solution(	["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))