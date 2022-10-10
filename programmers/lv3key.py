def isright(keys, locks, lock, M):
    for i in locks:
        if i not in keys:
            return False
    for j in keys:
        if 0<=j[0]<M and 0<=j[1]<M:
            if lock[j[0]][j[1]]==1:
                return False
    return True

def turn(keys, N):
    keys1 = []
    for i in keys:
        a, b = i
        keys1.append((b, N-a-1))
    return keys1

def function(keys, locks, lock, M):
    for i in range(len(locks)):
        lx, ly = locks[i]
        for j in range(len(keys)):
            kx, ky = keys[j]
            a, b = lx-kx, ly-ky
            super = []
            for k in keys:
                x, y = k
                super.append((x+a, y+b))
            if isright(super, locks, lock, M):
                return True            
    return False
    

def solution(key, lock):
    answer = False
    N = len(key)
    M = len(lock)
    keys = []
    locks = []
    for i in range(N):
        for j in range(N):
            if key[i][j]==1:
                keys.append((i, j))
    for i in range(M):
        for j in range(M):
            if lock[i][j]==0:
                locks.append((i, j))
    if not locks:
        return True
    elif not keys:
        return False
    elif len(locks)>len(keys):
        return False
    else:
        answer = function(keys, locks, lock, M)
        if answer:
            return answer
        keys1 = turn(keys, N)
        answer = function(keys1, locks, lock, M)
        if answer:
            return answer
        keys2 = turn(keys1, N)
        answer = function(keys2, locks, lock, M)
        if answer:
            return answer
        keys3 = turn(keys2, N)
        answer = function(keys3, locks, lock, M)
        return answer

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]	
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]	
print(solution(key, lock))