from itertools import combinations

n, m = map(int, input().split()) # 도시 크기, 남길 치킨집 개수
chicken, house = [], []
for r in range(n):
  data = list(map(int, input().split()))
  # 가정집, 치킨집 위치 저장
  for c in range(n):
    if data[c] == 1:
      house.append((r,c))
    elif data[c] == 2:
      chicken.append((r,c))

# 치킨집 중 M개를 고르는 모든 경우
candidates = list(combinations(chicken, m))

# 도시의 치킨 거리
def chicken_distance(candidate):
  result = 0
  # 모든 집에 대하여 가장 가까운 치킨집 찾기
  for hx, hy in house:
    temp = 1e9
    for cx, cy in candidate:
      temp = min((temp, abs(hx-cx) + abs(hy-cy)))
    # 가장 가까운 치킨집까지 거리
    result += temp
  return result

# 도시의 치킨 거리의 최솟값
result = 1e9
for candidate in candidates:
  result = min(result, chicken_distance(candidate))

print(result)