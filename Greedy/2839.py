# N 입력
N = int(input())
# 3kg와 5kg로 Nkg를 만들수 있는 모든 조합에서의 봉지 개수
n = []
# 모든 조합 확인 x = 5kg, y = 3kg
for x in range(1001):
    for y in range(1667):
        if (5 * x) + (3 * y) == N:
            n.append(x+y)

# 봉지 갯수가 1667개를 넘을 수는 없음, N < 5000이므로
s = 5000
# 모든 조합들 중 가장 작은 개수 추출
for i in n:
    s = min(s, i)

if s == 5000:
    print(-1)
else:
    print(s)