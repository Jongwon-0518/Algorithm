from sys import stdin
from collections import deque

N = int(stdin.readline())

answer1, answer2 = [0, 0, 0], [0, 0, 0]

for _ in range(N):
    a, b, c = map(int, stdin.readline().split())
    next_answer1, next_answer2 = [0]*3, [0]*3

    next_answer1[0] = max(answer1[0], answer1[1])+a
    next_answer1[1] = max(answer1)+b
    next_answer1[2] = max(answer1[1], answer1[2])+c

    next_answer2[0] = min(answer2[0], answer2[1])+a
    next_answer2[1] = min(answer2)+b
    next_answer2[2] = min(answer2[1], answer2[2])+c

    answer1 = next_answer1
    answer2 = next_answer2

print(max(answer1), min(answer2))
