import sys
input = lambda : sys.stdin.readline().strip()

# 내 풀이 - 미완성
n, m = map(int, input().split())
town = [list(map(int, input().split())) for _ in range(n)]
chicken = dict()


def get_dist(r1, c1, r2, c2):
    dist = abs(r1 - r2) + abs(c1 - c2)
    return dist


for i in range(n):
    for j in range(n):
        if town[i][j] == 2:
            chicken[(i, j)] = 0

for i in range(n):
    for j in range(n):
        if town[i][j] == 1:
            minn = get_dist(0, 0, n, n)
            for k in chicken.keys():
                if minn > get_dist(k[0], k[1], i, j):
                    minn = get_dist(k[0], k[1], i, j)
                chicken[k] += minn

print(min(chicken.values()))

'''
예제 1, 2는 성공했는데 그 이후는 모르겠어서 답 봄 
최소 거리 구하는 부분은 OK. m개의 치킨 집 고르는 부분에서 못하겠음ㅠㅠ
'''

# 정답
from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c)) # 일반 집
        elif data[c] == 2:
            chicken.append((r, c)) # 치킨집

# 모든 치킨 집 중에서 m개의 치킨 집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))

# 치킨 거리의 합을 계산하는 함수
def get_sum(candidate):
    result = 0
    # 모든 집에 대하여
    for hx, hy in house:
        # 가장 가까운 치킨 집을 찾기
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        # 가장 가까운 치킨 집까지의 거리를 더하기
        result += temp
    # 치킨 거리의 합 반환
    return result

# 치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)
