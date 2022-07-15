n = int(input()) # 삼각형의 크기
dp = [] # 한 번 계산한 결과를 저장할 DP 테이블
for i in range(n):
  input_data = list(map(int, input().split()))
  dp.append(input_data)

# 다이나믹 프로그래밍으로 2번째 층부터 확인
for i in range(1, n):
  for j in range(i + 1): # 각 층의 숫자들
    if j == 0: # 가장 왼쪽 숫자
      up_left = 0
    else:
      up_left = dp[i-1][j-1] # 좌측 상단
    if j == i: # 가장 오른쪽 숫자
      up = 0
    else:
      up = dp[i-1][j] # 우측 상단
    # 최대 합 저장
    dp[i][j] = dp[i][j] + max(up_left, up)

print(max(dp[n-1]))