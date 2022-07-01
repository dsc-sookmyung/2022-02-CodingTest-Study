def binary_search(array, start, end):
  if start > end: # 타겟이 리스트 안에 없을 때
    return None
  mid = (start + end) // 2 # 중간점
  if array[mid] == mid:
    return mid
  elif array[mid] > mid:
    return binary_search(array, start, mid-1) # 왼쪽 탐색
  else:
    return binary_search(array, mid+1, end) # 오른쪽 탐색

n = int(input())
array = list(map(int, input().split()))

index = binary_search(array, 0, n-1)

if index == None:
  print(-1)
else:
  print(index)