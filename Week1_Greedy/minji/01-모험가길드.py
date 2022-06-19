n = int(input())  # 모험가 수
fears = list(map(int, input().split())) # 각 모험가의 공포도
fears.sort() # 오름차순 정렬

group = 0 # 그룹 수
now = 0 # 현재 그룹에 포함된 모험가의 수

for fear in fears:
  now += 1 # 그룹에 추가
  # 현재 그룹에 포함된 모험가의 수 >= 현재 확인하고 있는 공포도이면 이를 그룹으로 설정
  if now >= fear:
    group += 1
    now = 0    
  
print(group)