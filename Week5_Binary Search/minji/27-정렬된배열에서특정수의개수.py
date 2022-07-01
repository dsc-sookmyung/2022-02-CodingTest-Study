n, x = map(int, input().split()) # 원소의 개수, 찾는 숫자
array = list(map(int, input().split())) # 수열

# 해당 숫자가 등장한 첫 번째 인덱스
def binary_search_first(array, target, start, end):
  if start > end: # 타겟이 리스트 안에 없을 때
    return None
  mid = (start + end) // 2 # 중간점
  # 해당 값을 가지는(array[mid] == target) 원소 중에 가장 왼쪽에 있는 경우에만 반환
  # 가장 왼쪽 인덱스(mid == 0)이거나, 바로 앞의 값이랑 같지 않을 때(target > array[mid-1])
  if array[mid] == target and (mid == 0 or target > array[mid-1]):
    return mid
  elif array[mid] >= target: # 타겟이 중간점보다 작거나, 같아도 가장 왼쪽은 아닐 때
    return binary_search_first(array, target, start, mid-1)
  elif array[mid] < target: # 타겟이 중간점보다 클 때
    return binary_search_first(array, target, mid+1, end)

# 해당 숫자가 등장한 마지막 인덱스
def binary_search_last(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  # 해당 값을 가지는(array[mid] == target) 원소 중에 가장 오른쪽에 있는 경우에만 반환
  # 가장 오른쪽 인덱스(mid == n-1)이거나, 바로 뒤의 값이랑 같지 않을 때(target < array[mid+1])
  if array[mid] == target and (mid == n-1 or target < array[mid+1]):
    return mid
  elif array[mid] > target: # 타겟이 중간점보다 작을 때
    return binary_search_last(array, target, start, mid-1)
  elif array[mid] <= target: # 타겟이 중간점보다 크거나, 같아도 가장 오른쪽은 아닐 때
    return binary_search_last(array, target, mid+1, end)

# 등장한 개수 세는 함수
def count_by_value(array, x):
  n = len(array)
  first = binary_search_first(array, x, 0, n-1)
  if first == None: # 원소가 없다면 -1 출력
    return -1
  last = binary_search_last(array, x, 0, n-1)

  return last - first + 1

print(count_by_value(array, x))