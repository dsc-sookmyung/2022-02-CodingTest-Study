n = int(input())

ugly = [0] * n # 못생긴 수를 담는 DP 테이블
ugly[0] = 1 # 첫 번째 못생긴 수=1

# 2배, 3배, 5배를 위한 인덱스
i2 = i3 = i5 = 0
# 처음에 곱셈값 초기화
next2, next3, next5 = 2, 3, 5

# 1부터 n까지 못생긴 수 찾기
for a in range(1, n):
  # 가능한 곱셈 값 중 최솟값 선택
  ugly[a] = min(next2, next3, next5)
  # 인덱스에 따라 곱셈 결과를 증가
  if ugly[a] == next2:
    i2 += 1
    next2 = ugly[i2] * 2
  if ugly[a] == next3:
    i3 += 1
    next3 = ugly[i3] * 3
  if ugly[a] == next5:
    i5 += 1
    next5 = ugly[i5] * 5

print(ugly[n-1])