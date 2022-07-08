n = int(input()) # 퇴사까지 남은 날
t = [] # 상담 기간
p = [] # 수익금
for _ in range(n):
  a, b = map(int, input().split())
  t.append(a)
  p.append(b)

d = [0] * (n + 1) # 한 번 계산한 결과를 저장할 DP 테이블
max_value = 0 # 최고 이익

# 뒤의 날짜부터 거꾸로 확인
for i in range(n-1, -1, -1):
  # 상담이 기간 안에 끝날 때
  if i + t[i] <= n:
    d[i] = max(p[i] + d[i + t[i]], max_value) # i일부터 상담을 시작했을 때 받을 수 있는 최대 금액
    max_value = d[i] # 그 값이 최고 이익
  # 기간을 벗어날 때
  else:
    d[i] = max_value

print(max_value)