from bisect import bisect_left, bisect_right

n, x = map(int, input().split()) # 원소의 개수, 찾는 숫자
array = list(map(int, input().split())) # 수열

# 값이 left_value, right_value인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
  right_index = bisect_right(array, right_value) # 가장 오른쪽 인덱스
  left_index = bisect_left(array, left_value) # 가장 왼쪽 인덱스
  return right_index - left_index

count = count_by_range(array, x, x)

if count == 0:
  print(-1)
else:
  print(count)