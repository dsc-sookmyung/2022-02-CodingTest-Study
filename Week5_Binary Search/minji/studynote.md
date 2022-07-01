# 이진 탐색

### 순차 탐색 (Sequential Search)

리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인

- 주로 정렬되지 않은 리스트에서 데이터를 찾을 때 사용
- 시간만 충분하다면 많은 데이터도 탐색 가능
- 데이터의 개수가 N개일 때 최대 N번의 비교 연산 필요 ⇒ 시간 복잡도 $O(N)$

**용도**

- 리스트에 특정 값의 원소가 있는지 체크할 때
- 특정한 값을 가지는 원소의 개수를 세는 count() 메서드

```python
def sequential_search(n, target, array):
  for i in range(n): # 앞에서부터 하나씩 확인하며
    if array[i] == target: # 찾고자 하는 단어와 동일한 경우
      return i + 1 # 현재 위치 반환

print("생성할 원소 개수와 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0]) # 원소의 개수
target = input_data[1] # 찾고자 하는 단어

print("원소 개수 만큼 문자열을 입력하세요. (띄어쓰기로 구분)")
array = input().split()

print(sequential_search(n, target, array))
```

### 이진 탐색 (Binary Search)

탐색 범위를 반으로 좁혀가며 빠르게 탐색

- 배열 내부 데이터가 정렬되어 있을 때만 사용 가능
- 찾으려는 데이터의 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터 탐색
- 확인하는 원소의 개수가 절반으로 줄어듦 ⇒ 시간 복잡도 $O(logN)$
- 탐색 범위가 2000만을 넘는 경우 고려해야 함
- 데이터의 개수 > 1000만 개, 탐색 범위의 크기 > 1000억 이상이라면 이진 탐색 알고리즘을 의심

**절차**

1. 시작점과 끝점을 확인한 후 둘 사이의 중간점을 정함 (중간점이 실수일 때는 소수점 이하 버림)
2. 찾으려는 데이터가 중간점보다 작으면 중간점 왼쪽 부분만, 크면 중간점 오른쪽 부분만 탐색 ⇒ 시작점과 끝점 조정
3. 1~2번을 반복해서 데이터를 찾는다.

**구현 방법**

1. 재귀 함수
    
    ```python
    def binary_search(array, target, start, end):
      if start > end: # 타겟이 리스트 안에 없을 때
        return None
      mid = (start + end) // 2 # 중간점
      if array[mid] == target: # 타겟이 중간점에 있을 때
        return mid
      elif array[mid] > target: # 타겟이 중간점보다 작을 때
        return binary_search(array, target, start, mid-1) # 왼쪽 이진탐색
      elif array[mid] < target: # 타겟이 중간점보다 클 때
        return binary_search(array, target, mid+1, end) # 오른쪽 이진탐색
     
    n, target = list(map(int, input().split())) # 원소 개수, 찾으려는 원소
    array = list(map(int, input().split())) # 전체 원소
    
    result = binary_search(array, target, 0, n-1) # 이진탐색 실행
    if result == None:
      print("원소가 존재하지 않습니다.")
    else:
      print(result + 1)
    ```
    
2. 단순 반복문
    
    ```python
    def binary_search(array, target, start, end):
      while start <= end:
        mid = (start + end) // 2 # 중간점
        if array[mid] == target: # 타겟이 중간점에 있을 때
          return mid
        elif array[mid] > target: # 타겟이 중간점보다 작을 때
          end = mid - 1
        else: # 타겟이 중간점보다 클 때
          start = mid + 1
      return None # 값이 없을 때
    
    n, target = list(map(int, input().split()))
    array = list(map(int, input().split()))
    
    result = binary_search(array, target, 0, n-1)
    if result == None:
      print("원소가 존재하지 않습니다.")
    else:
      print(result + 1)
    ```
    

### 트리 자료구조

그래프 자료구조의 일종으로 DB, 파일 시스템 등 많은 양, 계층적이고 정렬된 데이터 관리 목적으로 사용

![](https://user-images.githubusercontent.com/61882016/176926898-a6922ec0-0467-4aa1-ae5b-71153046ae1f.png)

- 노드: 정보의 단위, 어떤 정보를 가지고 있는 개체 (5장에서와 동일)
- 트리: 부모 노드와 자식 노드의 관계로 표현
- 루트 노드: 트리의 최상단 노드
- 단말 노드: 트리의 최하단 노드
- 서브 트리: 트리의 일부를 떼어낸 트리 구조

### 이진 탐색 트리

트리 자료구조 중에서 가장 간단한 형태

이진 탐색이 동작할 수 있도록 고안된 효율적 탐색이 가능한 자료구조

![image](https://user-images.githubusercontent.com/61882016/176927057-ee37dbb3-5fa9-4481-8cde-e8a70f61be09.png)

- 왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드
- 이진 탐색 트리를 구현하는 문제보다는 데이터를 조회하는 과정을 위주로 공부

![image](https://user-images.githubusercontent.com/61882016/176927287-3d3fa17b-ae4a-4288-a363-bb981140908f.png)

1. 루트 노드부터 방문 → 찾으려는 원소값이 더 크면 오른쪽 자식 노드를, 더 작으면 왼쪽 자식 노드를 방문
2. 해당 자식 노드를 부모 노드라고 생각하며 1번 과정을 반복
3. 노드 값과 찾는 값이 동일하면 탐색 종료

**빠르게 입력받기**

입력 데이터가 많을 때는 input() 대신 sys 라이브러리의 `readline()` 함수를 이용하여 시간초과 방지

- `rstrip()`: 소스코드에 readline()으로 입력하면 입력 후 엔터가 줄 바꿈 기호로 입력되므로, 해당 공백 문자 제거하는 함수

```python
import sys
input_data = sys.stdin.readline().rstrip() # 하나의 문자열 데이터 입력받기
```

### 실전 1 - 부품 찾기

- **문제**: N개의 부품에 고유한 부품 번호가 있다. 손님이 요청한 부품 M개가 각각 있는지 확인하라
- **풀이**: 이진 탐색 알고리즘
    - 매장 내 N개의 부품을 번호 기준으로 정렬
    - M개의 찾고자 하는 부품이 각각 매장에 존재하는지 검사
- **비고**: 시간 복잡도 $O((M+N)*logN)$

```python
def binary_search(array, target, start, end):
  if start > end: # 타겟이 리스트 안에 없을 때
    return None
  mid = (start + end) // 2 # 중간점
  if array[mid] == target: # 타겟이 중간점에 있을 때
    return mid
  elif array[mid] > target: # 타겟이 중간점보다 작을 때
    return binary_search(array, target, start, mid-1) # 왼쪽 이진탐색
  elif array[mid] < target: # 타겟이 중간점보다 클 때
    return binary_search(array, target, mid+1, end) # 오른쪽 이진탐색

n = int(input())
array = list(map(int, input().split())) # 전체 부품
array.sort() # 오름차순 정렬

m = int(input())
x = list(map(int, input().split())) # 손님이 요청한 부품

for i in x:
  result = binary_search(array, i, 0, n-1) # 이진탐색 실행
  if result != None:
    print('yes', end=' ')
  else:
    print('no', end=' ')
```

- **풀이 2**: 계수 정렬
    - 모든 원소의 번호를 포함하는 크기의 리스트를 만들어 해당 인덱스의 값이 1인지 확인
- **풀이 3**: 집합 자료형 set() 활용
    - if (데이터) in (리스트):

### 실전 2 - 떡볶이 떡 만들기 (*)

- **문제**: 제각기 다른 높이의 떡을 절단기에 넣고 높이 H를 지정하면 한 번에 절단하고, 이 때 잘라낸 길이의 떡을 손님이 가져간다. 손님이 요청한 길이 M만큼 떡을 얻기 위해 절단기에서 설정해야 할 높이 H의 최댓값은?
- **풀이**: 이진 탐색 문제, 파라메트릭 서치(Parametric Search) 유형
    - 파라메트릭 서치: 최적화 문제를 결정 문제(예 or 아니오로 대답)로 바꾸어 해결하는 기법
    - 적절한 높이를 찾을 때까지 절단기 높이 H를 반복해서 조정
    - 조건 만족 여부(예 or 아니오)에 따라서 이진 탐색으로 탐색 범위 좁혀나가기
- 예시: [19, 15, 10, 17], m=6 ⇒ H의 최댓값=15
    1. 시작점=0, **끝점=떡 길이 최댓값**, 중간점=절단기 높이 H로 설정하고 떡을 자름
        1. H=(0+19)//2=9 ⇒ M=10+6+1+8=25
        2. 6보다 크므로 오른쪽 리스트를 이진 탐색
    2. 시작점=10, 끝점=19, 중간점 H=(10+19)//2=14 ⇒ M=5+1+0+3=9
        1. 6보다 크므로 오른쪽 리스트를 이진 탐색
    3. 시작점=15, 끝점=19, 중간점 H=(15+19)//2=17 ⇒ M=2+0+0+0=2
        1. 6보다 작으므로 왼쪽 리스트를 이진 탐색
    4. 시작점=15, 끝점=16, **중간점=15** ⇒ M=4+0+0+2=**6**
        1. 6과 같으므로 탐색 종료
- **비고**: 0 ≤ 절단기 높이 ≤ 10억이므로 순차 탐색은 시간 초과
    - 이진 탐색: 31번 만에 모든 경우의 수 고려 가능
    - 떡의 개수 ≤ 100만 ⇒ 최대 3000만 번 정도의 연산 ⇒ 시간 제한 2초 안에 가능
    - 재귀 함수보다 반복문을 이용하면 간결하게 구현 가능

```python
n, m = map(int, input().split()) # 떡의 개수, 요청한 떡의 길이
array = list(map(int, input().split())) # 떡의 개별 높이
result = 0

def binary_search(array, start, end):
  while start <= end:
    total = 0 # 절단한 길이의 합
    mid = (start + end) // 2 # 중간점
    for x in array:
      # 잘랐을 때의 떡의 길이
      if x > mid:
        total += (x - mid)
    if total < m: # 요청한 길이보다 작을 때
      end = mid - 1
    else: # 요청한 길이보다 클 때
      result = mid # 최대한 덜 잘랐을 때가 정답이므로 여기에서 result에 기록
      start = mid + 1
  return result

print(binary_search(array, 0, max(array)))
```
