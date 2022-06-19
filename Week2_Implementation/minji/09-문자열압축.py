def solution(s):
  answer = []

  # 1부터 (문자열 길이 / 2) 까지의 모든 수를 단위로 하여 조사
  for cut in range(1, len(s) // 2 + 1):
    compressed = "" # 압축 결과
    prev = s[0:cut] # 앞에서부터 단위(cut개) 만큼 추출
    repeat = 1 # 반복된 횟수

    # 단위 크기만큼 증가시키며 이전 문자열과 비교
    for j in range(cut, len(s), cut):
      if prev == s[j:j+cut]: # 같을 때
        repeat += 1
      else: # 다를 때
        compressed += str(repeat) + prev if repeat >= 2 else prev # 문자의 개수와 반복되는 값으로 표현 (repeat=1일 때 생략)
        prev = s[j:j+cut] # 타겟 변경
        repeat = 1
    
    # 남아있는 문자열 처리 (*)
    compressed += str(repeat) + prev if repeat >= 2 else prev
    answer.append(len(compressed))

  # 압축되는 문자열 길이 중 최솟값
  return min(answer)