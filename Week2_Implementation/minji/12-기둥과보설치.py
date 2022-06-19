# 현재 구조물이 정상인지 확인하는 함수
def possible(answer):
  for x, y, stuff in answer:
    if stuff == 0: # 기둥
      # 바닥 위 or 보의 한쪽 끝부분 위 or 다른 기둥 위
      if y == 0 or [x-1, y, 1] in answer or [x, y-1, 0] in answer:
        continue
      return False # 아니라면 거짓 반환
    elif stuff == 1: # 보
      # 한쪽 끝부분이 기둥 위 or 양쪽 끝부분이 다른 보와 동시에 연결
      if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
        continue
      return False # 아니라면 거짓 반환
  return True


def solution(n, build_frame):
  answer = []

  for frame in build_frame:
    x, y, stuff, operate = frame
    if operate == 0: # 삭제하는 경우
      answer.remove([x, y, stuff]) # 일단 삭제해본 뒤
      if not possible(answer): # 가능한 구조물이 아니라면
        answer.append([x, y, stuff]) # 다시 설치
    if operate == 1: # 설치하는 경우
      answer.append([x, y, stuff]) # 일단 설치해본 뒤
      if not possible(answer): # 가능한 구조물이 아니라면
        answer.remove([x, y, stuff]) # 다시 삭제

  return sorted(answer) # 정렬된 결과 반환


print(solution(5, [[0,0,0,1], [2,0,0,1], [4,0,0,1], [0,1,1,1], [1,1,1,1], [2,1,1,1], [3,1,1,1], [2,0,0,0], [1,1,1,0], [2,2,0,1]]))