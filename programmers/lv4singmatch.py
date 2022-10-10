# def match(id1, id2):
#     id1_n = len(id1)
#     id2_n = len(id2)
#     i = 0
#     correct = True
#     if id1_n != id2_n:
#         return False
#     elif id1_n == id2_n:
#         if id1 == '?'*id1_n:
#             return True
#         while i<id1_n:
#             if id1[i]==id2[i] or id1[i]=='?':
#                 i += 1
#             else:
#                 correct = False
#                 break
#         return correct

# def match1(id1, id2):
#     if id1[-1] == "?":
#         id1_not = id1.replace("?", "")
#         k = len(id1_not)
#         if id1_not == id2[:k]:
#             return True
#     else:
#         id1_not = id1.replace("?", "")
#         k = len(id1_not)
#         if id1_not == id2[-k:]:
#             return True

# def solution(words, queries):
#     n = len(queries)
#     answer = {}
#     for i in range(n):
#         x = queries[i]
#         for j in words:
#             if len(x)==len(j):
#                 if x == "?"*len(x):
#                     answer[i] += 1
#                 elif match1(x, j):
#                     answer[i] += 1
#     return answer


# Trie 구조

class Trie():
    def __init__(self):
        self.val = 0
        self.next = dict()
    def __repr__(self):
        return f'{self.val} {self.next}'

def makeTrie(words):
    trie, r_trie = dict(), dict()
    for word in words:
        l = len(word)
        trie[l], r_trie[l] = trie.get(l, dict()), r_trie.get(l, dict())
        trie[l][word[0]] = trie[l].get(word[0], Trie())
        r_trie[l][word[-1]] = r_trie[l].get(word[-1], Trie())
        cur, cur_r = trie[l][word[0]], r_trie[l][word[-1]]
        for c, c_r in zip(word[1:], word[::-1][1:]):
            cur.val += 1
            cur_r.val += 1
            cur.next[c], cur_r.next[c_r] = cur.next.get(c, Trie()), cur_r.next.get(c_r, Trie())
            cur, cur_r = cur.next[c], cur_r.next[c_r]
        cur.val += 1
        cur_r.val += 1
    return trie, r_trie

def searchTrie(trie, r_trie, query):
    l = len(query)
    if query[0] != '?':
        if trie.get(l) is None: return 0, None
        return trie[l], False
    elif query[-1] != '?':
        if r_trie.get(l) is None: return 0, None
        return r_trie[l], True
    else:
        if trie.get(l) is None: return 0, None
        return sum(v.val for v in trie[l].values()), None

def countWords(query, cur, isReverse):
    if isReverse is None: return cur
    if isReverse: query = query[::-1]
    for q in query:
        if q == '?': return sum(v.val for v in cur.values())
        if cur.get(q) is None: return 0
        cur = cur[q].next
    return 1

def solution(words, queries):
    trie, r_trie = makeTrie(words)
    return [countWords(query, *searchTrie(trie, r_trie, query)) for query in queries]


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]	
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]	
print(solution(words, queries))