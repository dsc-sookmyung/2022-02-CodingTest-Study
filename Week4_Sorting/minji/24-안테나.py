# 해설지 풀이
# n = int(input())
# houses = list(map(int, input().split()))
# houses.sort()
# print(houses[(n-1) // 2]) # 위치 인덱스의 중간값


# 나의 플이
n = int(input())
houses = list(map(int, input().split()))
result = []

# 각 집에 안테나 설치해보고 거리 총합 계산
for antenna in houses:
  distance_sum = 0
  for house in houses:
    distance_sum += abs(house - antenna)
  result.append((antenna, distance_sum)) # (안테나 위치, 거리 총합) 정보 저장

# 거리 총합이 작은 순서대로 정렬(같으면 안테나 위치가 작은 순서대로)
result.sort(key = lambda x: (x[1], x[0]))
print(result[0][0])