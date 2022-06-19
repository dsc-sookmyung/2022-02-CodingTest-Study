from itertools import permutations

def solution(n, weak, dist):
  # 길이를 2배로 늘려 원형을 일자 형태로
  length = len(weak)
  for i in range(length):
    weak.append(weak[i] + n)
  answer = len(dist) + 1 # 투입할 친구의 최솟값 (전체 친구 + 1로 초기화)

  for start in range(length): # 시작점(첫 1바퀴)
    # 친구를 나열하는 모든 경우의 수
    for friends in list(permutations(dist, len(dist))):
      count = 1 # 투입할 친구 수
      # 해당 친구가 점검할 수 있는 마지막 위치
      position = weak[start] + friends[count - 1]
      # 시작점부터 모든 취약 지점을 확인
      for index in range(start, start + length):
        # 점검할 수 있는 위치를 벗어난 경우
        if position < weak[index]:
          count += 1 # 새로운 친구 투입
          # 더 투입할 친구가 없으면 종료
          if count > len(dist):
            break
          position = weak[start] + friends[count - 1]
      answer = min(answer, count)
  
  # 친구들을 모두 투입해도 취약 지점을 모두 점검할 수 없는 경우
  if answer > len(dist):
    return -1

  return answer

print(solution(12, [1,5,6,10], [1,2,3,4]))
print(solution(12, [1,3,4,9,10], [3,5,7]))