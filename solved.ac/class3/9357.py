from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    n = int(stdin.readline())
    dic = {}
    for _ in range(n):
        name, category = stdin.readline().split()

        if category in dic:
            dic[category].append(name)
        else:
            dic[category] = [name]
    
    answer = 1

    for i in dic:
        answer *= len(dic[i])+1

    answer -= 1
    print(answer)