# 정렬(Sorting)

데이터를 특정한 기준에 따라 순서대로 나열하는 것

- 종류: 선택 정렬, 삽입 정렬, 퀵 정렬, 계수 정렬
- 이진 탐색(Binary Search)의 전처리 과정
- 리스트 뒤집기(reverse): 시간 복잡도 $O(N)$

### 선택 정렬(Selection Sort)

매번 가장 작은 데이터를 선택하는 알고리즘

1. 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 교환
2. 정렬이 완료된 곳은 제외하고, 나머지 부분에서 1번 과정 수행 (`N-1`번 반복)
3. 마지막 데이터는 가만히 놔두어도 정렬 완료

```python
for i in range(len(array)):
  min_index = i # 가장 작은 원소의 인덱스
  for j in range(i+1, len(array)):
    if array[min_index] > array[j]:
      min_index = j # 최솟값 인덱스 찾아서
  array[i], array[min_index] = array[min_index], array[i] # 자리 바꾸기
```

- 평균 시간 복잡도: $O(N^2)$
    - (N-1)번 만큼 비교 연산 → 작은 수를 찾아 맨 앞으로 보내는 작업
    - 연산 횟수 = N + (N-1) + (N-2) + … + 2 ≒ N * (N+1) / 2 = (N²+N) / 2
    - 반복문 2중 중첩
    - N > 10,000 일 때 비효율적

### 삽입 정렬

데이터를 앞에서부터 하나씩 확인하며 적절한 위치에 삽입

- 필요할 때만 위치를 바꿈 ⇒ 데이터가 거의 정렬되어 있을 때 훨씬 효율적
- 적절한 위치에 들어가기 전에, 그 앞까지의 데이터는 이미 정렬되어 있음
- 삽입될 위치를 찾기 위해 왼쪽으로 한 칸씩 이동할 때, 삽입될 데이터보다 작은 데이터를 만나면 그 위치에서 멈춤
1. 첫 번째 데이터는 그 자체로 정렬되어 있다고 판단, 두 번째 데이터가 들어갈 위치를 판단 (첫 번째 데이터의 왼쪽 or 오른쪽)
2. 세 번째 데이터가 들어갈 위치 판단 (1번째, 2번째 데이터와 비교) → … → N번째 데이터까지 `N-1`번 반복

```python
for i in range(1, len(array)): # 두 번째 데이터부터 판단
  for j in range(i, 0, -1): # i부터 1까지 한 칸씩 왼쪽으로 이동
    if array[j] < array[j-1]: # 한 칸씩 왼쪽으로 이동하며
      array[j], array[j-1] = array[j-1], array[j] # 자리 바꾸기
    else: # 삽입될 데이터보다 작은 데이터를 만나면 멈춤
      break
```

- 평균 시간 복잡도: $O(N^2)$
    - 반복문 2중 중첩
    - 최선의 경우 $O(N)$: 데이터가 거의 정렬되어 있을 때

### 퀵 정렬

기준 데이터 설정 ⇒ 기준보다 큰 데이터와 작은 데이터의 위치를 바꿈 ⇒ 리스트를 반으로 분할

- 피벗(Pivot): 교환하기 위한 기준
    - 호어 분할 방식: 리스트에서 첫 번째 데이터를 피벗으로 정하는 분할 방식
- 재귀 함수의 동작 원리와 동일
1. 
    1. 첫 번째 데이터를 피벗으로 지정: 왼쪽에서 피벗보다 큰 데이터를, 오른쪽에서 피벗보다 작은 데이터를 선택 ⇒ 위치 변경
    2. 두 값이 엇갈린 경우, 작은 데이터와 피벗의 위치를 변경
    3. 분할 완료: 이제 피벗의 왼쪽은 피벗보다 작은 값이, 오른쪽은 피벗보다 큰 값이 위치
2. 왼쪽, 오른쪽 리스트도 동일한 방식으로 정렬
3. 과정을 반복하여 리스트의 원소가 1개가 되면 정렬 완료

```python
# 직관적인 형태
def quick_sort(array, start, end):
  # 원소가 1개이면 종료
  if start >= end:
    return
  pivot = start # 피벗 = 첫 번째 원소
  left = start + 1
  right = end
  while left <= right:
    # 피벗보다 큰 데이터를 찾기
    while left <= end and array[left] <= array[pivot]:
      left += 1
    # 피벗보다 작은 데이터 찾기
    while right > start and array[right] >= array[pivot]:
      left -= 1
    # 엇갈린 경우 작은 데이터와 피벗의 위치를 변경
    if left > right:
      array[right], array[pivot] = array[pivot], array[right]
    # 엇갈리지 않은 경우 큰 값과 작은 값의 위치를 변경
    else:
      array[left], array[right] = array[right], array[left]
  # 왼쪽, 오른쪽 리스트도 정렬
  quick_sort(array, start, right-1)
  quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)

# 파이썬의 장점을 살린 간결한 형태
def quick_sort(array):
  # 원소가 1개이면 종료
  if len(array) <= 1:
    return array
  pivot = array[0] # 피벗 = 첫 번째 원소
  tail = array[1:] # 피벗 제외한 리스트
  left_side = [x for x in tail if x <= pivot] # 피벗보다 작은 부분
  right_side = [x for x in tail if x > pivot] # 피벗보다 큰 부분
  # 왼쪽, 오른쪽 리스트도 정렬하고 합치기
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
```

- 평균 시간 복잡도: $O(NlogN)$
    - 데이터가 N개일 때, 분할이 일어나는 횟수 ≒ $logN$(밑이 2)
    - 최악의 경우 $O(N^2)$: 리스트의 가장 왼쪽 데이터를 피벗으로 삼을 때, 이미 데이터가 정렬되어 있을 때
    - 파이썬 기본 정렬 라이브러리 이용하면 $O(NlogN)$ 보장
    

### 계수 정렬

특정한 값을 가지는 데이터의 개수를 카운트

- 모든 범위를 담을 수 있는 크기의 리스트 선언
- 데이터의 크기가 한정되어 있고, 중복된 값이 많을 수록 유리
    - 정수 형태로 표현할 수 있을 때만 사용 가능
    - 큰 데이터 - 작은 데이터 ≤ 1,000,000일 때 효과적
- 데이터의 개수가 많아도 매우 빠르게 동작
1. 최댓값과 최솟값의 범위를 모두 포괄하는 리스트 생성, 0으로 모두 초기화
2. 데이터를 하나씩 확인하며 데이터의 값과 동일한 인덱스의 값을 1씩 증가 ⇒ 등장 횟수
3. 해당 리스트를 순서대로 등장한 횟수만큼 출력

```python
# 모든 범위를 포함하는 리스트 선언
count = [0] * (max(array) - min(array) + 1)

# 각 데이터에 해당하는 인덱스 값 증가
for i in range(len(array)):
  count[array[i]] += 1

# 해당 리스트를 순서대로 등장한 횟수만큼 출력
for i in range(len(count)):
  for j in range(count[i]):
    print(i, end=' ')
```

- 평균 시간 복잡도: $O(N+K)$ (K=데이터 중 최댓값)
- 평균 공간 복잡도: $O(N+K)$
    - 0과 999,999 두 개만 있어도 리스트의 크기가 100만 개 ⇒ 때에 따라 비효율적
    - 동일한 값을 가지는 데이터가 여러 개 등장할 때 효율적
    

### 정리

| 정렬 알고리즘 | 평균 시간 복잡도 | 공간 복잡도 | 특징 |
| --- | --- | --- | --- |
| 선택 정렬 | O(N²) | O(N) | 가장 작은 데이터를 선택 ⇒ 정렬되지 않은 데이터 중 가장 앞쪽 데이터와 위치 교환 / 아이디어가 매우 간단 |
| 삽입 정렬 | O(N²) | O(N) | 데이터를 앞에서부터 하나씩 확인하며 적절한 위치에 삽입 / 데이터가 거의 정렬되어 있을 때는 가장 빠름 |
| 퀵 정렬 | O(NlogN) | O(N) | 기준 데이터 설정 ⇒ 기준보다 큰/작은 데이터의 위치를 바꿈 / 대부분의 경우 가장 적합, 충분히 빠름 |
| 계수 정렬 | O(N+K)(K=데이터 중에서 가장 큰 양수) | O(N+K)(K=데이터 중에서 가장 큰 양수) | 특정한 값을 가지는 데이터의 개수를 카운트 / 데이터의 크기가 한정된 경우에만 사용 가능, 매우 빠르게 동작 |

### Python의 정렬 라이브러리

1. sorted(): 항상 리스트 자료형 반환
2. sort(): 리스트 객체의 내장 함수
- key 매개변수
    - lambda 함수: 함수를 한 줄에 간단하게 작성, 이름 없는 함수
        
        lambda 매개변수: 리턴값
        
        ```python
         # 일반적인 add() 메서드
        def add(a, b):
          return a + b
        print(add(2, 6))
        
        # 람다 표현식
        print((lambda a,b: a+b)(3,7))
        
        array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]
        
        def my_key(x):
          return x[1]
        
        # sorted 함수로 오름차순 정렬 (점수 기준)
        print(sorted(array, key=my_key))
        print(sorted(array, key=lambda x: x[1]))
        ```
        
- 시간 복잡도: 최악의 경우에도 $O(NlogN)$ 보장

### 실전 1 - 위에서 아래로

- **문제**: 주어진 n개의 수를 내림차순 정렬하여 출력
- **풀이**: 파이썬 기본 정렬 라이브러리 활용: sort() / sorted()
- **비고**: 1 ≤ n ≤ 100,000 ⇒ 어떤 정렬 알고리즘을 활용해도 무방

```python
n = int(input())

array = []
for _ in range(n):
  array.append(int(input()))

array = sorted(array, reverse=True) # 내림차순 정렬

for i in array:
  print(i, end=' ')
```

### 실전 2 - 성적이 낮은 순서로 학생 출력하기

- **문제**: 학생 N명의 성적이 낮은 순서대로 이름 출력
- **풀이**: 파이썬 기본 정렬 라이브러리 활용: sort() / sorted()
    - 학생 정보를 (점수, 이름)으로 묶고, 점수를 기준으로 오름차순 정렬 → key 속성에 lambda 함수
- **비고**: 1 ≤ n ≤ 100,000 ⇒ 시간 복잡도 $O(NlogN)$ 보장하는 알고리즘

```python
n = int(input())

students = []
for _ in range(n):
  students.append(input().split())

students.sort(key=lambda x: int(x[1])) # 점수를 기준으로 오름차순 정렬

for student in students:
  print(student[0], end=' ')
```

### 실전 3- 두 배열의 원소 교체

- **문제**: 바꿔치기 연산을 통해 만들 수 있는 배열 A의 모든 원소의 합의 최댓값
    - 바꿔치기 연산=배열 A의 원소 하나와 배열 B의 원소 하나를 바꾸기
    - 두 배열의 원소 개수=N, 바꿔치기 연산=최대 K회
- **풀이**:
    - A에서는 최대한 작은 수를, B에서는 최대한 큰 수를 바꿔치기 해야 함
    - A는 오름차순, B는 내림차순 정렬
    - A의 원소 값 < B의 원소 값일 때만 바꿔치기 연산 (최대 K번) - 인덱스 0번~(k-1)번
- **비고**: 1 ≤ N ≤ 100,000, 0 ≤ K ≤ N ⇒ 시간 복잡도 $O(NlogN)$ 보장하는 알고리즘

```python
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() # 오름차순 정렬
b.sort(reverse=True) # 내림차순 정렬

#  A의 원소 값 < B의 원소 값일 때만 바꿔치기 연산
for i in range(k):
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]
  else:
    break

print(sum(a))
```
