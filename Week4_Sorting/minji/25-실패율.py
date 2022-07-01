def solution(N, stages):
  players = len(stages) # 도전자 수
  fail_list = [] # 스테이지 별 실패율

  for stage in range(1, N+1):
    count = stages.count(stage) # 해당 스테이지에 머물러있는 사람
    if players == 0: # 도전자가 없으면 실패율 = 0
      fail = 0
    else:
      fail = count / players
    fail_list.append((stage, fail))
    players -= count # 실패자는 다음 스테이지 카운트에서 제외

  fail_list.sort(key = lambda x: -x[1])
  return [i[0] for i in fail_list]

print(solution(5, [2,1,2,6,2,4,3,3]))