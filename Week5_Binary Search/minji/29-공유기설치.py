n, c = map(int, input().split()) # 집 수, 공유기 수
house = []
for _ in range(n):
  house.append(int(input()))

house.sort() # 오름차순 정렬

start = house[1] - house[0] # 최소 간격
end = house[-1] - house[0] # 최대 간격
result = 0

while(start <= end):
  mid = (start + end) // 2 # 중간점
  value = house[0]
  count = 1
  for i in range(1, n): # 공유기 설치
    if house[i] >= value + mid:
      value = house[i]
      count += 1
  if count >= c: # 더 설치 가능할 때
    start = mid + 1 # 거리 증가
    result = mid # 최적의 결과를 저장
  else: # 더 설치 불가
    end = mid - 1 # 거리 감소

print(result)