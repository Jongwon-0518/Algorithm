import math
def function(n, k):
    answer = []
    while True:
        answer.append(n%k)
        n = n//k
        if n == 0:
            break
    answer.reverse()
    return answer

def solution(n, k):
    answer = 0
    a = function(n, k)
    num = []
    i = 0
    while i<len(a):
        if a[i] != 0:
            for j in range(i, len(a)): 
                if a[j] == 0:
                    num.append(a[i:j])
                    i = j-1
                    break
                elif j == len(a)-1:
                    num.append(a[i:])
                    i = j
                    break
        i += 1
    
    d = []
    for i in num:
        b = []
        for j in i:
            b.append(str(j))
        c = ''.join(b)
        d.append(int(c))

    for i in d:
        if i != 1:
            j = 2
            while j<int(math.sqrt(i)+1):
                if i%j==0:
                    break
                j += 1
            if j>=int(math.sqrt(i)+1):
                answer += 1
                
    return answer

print(solution(437674, 3))