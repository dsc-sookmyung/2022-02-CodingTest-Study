def edit_dist(str1, str2):
  n = len(str1)
  m = len(str2)

  dp = [[0] * (m + 1) for _ in range(n + 1)] # n*m 크기의 dp 테이블
  # dp 테이블 초기 설정
  for r in range(1, n + 1):
    dp[r][0] = r
  for c in range(1, m + 1):
    dp[0][c] = c
  
  # 최소 편집 거리
  for r in range(1, n + 1):
    for c in range(1, m + 1):
      # 두 문자가 같은 경우: 왼쪽 위에 있는 수를 그대로 대입
      if str1[r-1] == str2[c-1]:
        dp[r][c] = dp[r-1][c-1]
      # 두 문자가 다른 경우: 삽입(왼쪽), 삭제(위쪽), 교체(왼쪽 위) 중 최솟값에 + 1 대입
      else:
        dp[r][c] = 1 + min(dp[r][c-1], dp[r-1][c], dp[r-1][c-1])

  return dp[n][m]

a = input()
b = input()
print(edit_dist(a, b))