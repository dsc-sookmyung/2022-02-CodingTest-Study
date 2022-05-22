# 그리디(Greedy), 탐욕법

현재 상황에서 지금 당장 좋은 것만 고르는 방법

- 기준에 따라 좋은 것을 선택하는 알고리즘
- 문제에서 _가장 큰/작은 순서대로_ 등의 기준을 제시
- 주로 정렬 알고리즘과 짝을 이루어 출제
- 문제를 풀 때 먼저 탐욕적인 해결법이 존재하는지 고려
- 최적의 해를 찾기 위한 정당성 검토 필요
- 다익스트라, 크루스칼 알고리즘 등이 속함

### 예제 1 - 거스름돈

- **문제**: 거슬러 줘야 할 돈이 N원일 때 필요한 동전의 최소 개수 (거스름돈: 500/100/50/10)
- **풀이**: 가장 큰 화폐 단위부터 돈을 거슬러주기
    - 화폐 종류(K개)만큼 반복 수행 ⇒ O(K)
- **비고**: 화폐 단위가 작은 단위의 배수일 때 성립 ⇒ 정당성 검토 필요

```python
n = 1260 # 잔돈
count = 0

# 큰 단위의 화페부터 차례로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
  count += n // coin # 해당 화폐로 거슬러줄 수 있는 동전 개수
  n %= coin # 남은 거스름돈

print(count)
```

### 실전 1 - 큰 수의 법칙

- **문제**: 배열(크기=N)에 주어진 수들을 M번 더하여 가장 큰 수를 만들어라
    - 단, 배열의 특정 인덱스에 있는 수가 연속해서 K번까지만 더해질 수 있음 (수는 같아도 인덱스가 다르면 서로 다름)
    - K ≤ M
    - ex) [2,4,5,4,6], M=8, K=3 ⇒ 6+6+6+5+6+6+6+5 = 46
- **풀이 1**: 가장 큰 수를 K번, 다음으로 큰 수를 1번, ...(반복)
- **비고**: M의 크기가 100억 이상으로 커지면 시간 초과

```python
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort() # 오름차순 정렬
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두 번째로 큰 수

result = 0

while True:
  for i in range(k):
    if m == 0:
      break
    result += first # 가장 큰 수를 k번 더하기
    m -= 1 # 더해야 할 횟수 1 차감
  if m == 0: # m=0이면 반복문 탈출
    break
  result += second # 두번째로 큰 수를 1번 더하기
  m -= 1 # 더해야 할 횟수 1 차감
  
print(result)
```

- **풀이 2**: 반복되는 수열 파악
    - 수열의 길이: (K+1)
    - 수열의 반복 횟수: M을 (K+1)로 나눈 몫
        - 나누어 떨어지지 않을 때: 그 나머지만큼 가장 큰 수가 더해짐
    - ex) (6+6+6+5) + (6+6+6+5) ⇒ 수열 길이는 K+1 = 3+1 = 4, 수열 반복 횟수는 M//(K+1) = 8//4 = 2
    - 가장 큰 수가 더해지는 횟수(count): `int(M/(K+1)) * K + M%(K+1)`
    - 두 번째로 큰 수가 더해지는 횟수: `M - count`

```python
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort() # 오름차순 정렬
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수
count = int(m/(k+1)) * k
count += m % (k+1)

result = 0
result += (count)*first # 가장 큰 수 더하기
result += (m-count)*second # 두 번째로 큰 수
  
print(result)
```
### 실전 2 - 숫자 카드 게임

- **문제**: N * M 크기의 카드 중 룰에 맞게 카드를 뽑기
    1. 뽑으려는 카드가 포함된 행 선택
    2. 선택된 행 중 가장 숫자가 낮은 카드를 뽑아야 함
    3. 예) 3 1 2 / 4 1 4 / 2 2 2 ⇒ 3행 선택 ⇒ `2` 선택
- **풀이**: 각 행마다 가장 작은 수를 찾음 ⇒ 그 중 가장 큰 수
    - 각 행마다 가장 작은 수를 `min_value`에 저장
    - `max` 함수로 result와 비교하여 최댓값만 저장
- **비고**: 각 숫자는 1 이상 10,000 이하

```python
n, m = map(int, input().split())

result =  0
for i in range(n):
  data = list(map(int, input().split()))
  min_value = min(data) # 가장 작은 수
  result = max(result, min_value) # 가장 작은 수들 중 최댓값

print(result)
```

### 실전 3 - 1이 될 때까지

- **문제**: 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 수행하려고 한다. 수행해야 하는 최소 횟수는?
    1. N에서 1 빼기
    2. N을 K로 나누기 (나누어 떨어질 때만)
    - 조건: 2 ≤ n ≤ k ≤ 100,000
- **풀이**: N이 K로 나누어 떨어질 때까지 1을 빼기(1번) → N을 K로 나누기(2번) → …
- **비고**: N이 클 수록 K로 나눴을 때 더 많이 감소 ⇒ K로 최대한 많이 나눌 수 있는 것이 최적의 해를 보장

```python
n, k = map(int, input().split())
result =  0

# n이 k 이상이라면 반복 수행
while n >= k:
  # n이 나누어 떨어질 때까지 1을 빼기 (1번)
  while n % k != 0:
    n -= 1
    result += 1
  # n을 k로 나누기(2번)
  n //= k
  result += 1

# n이 k 미만이 되면 n=1이 될 때까지 1을 빼기
while n > 1:
  n -= 1
  result += 1

print(result)
```

- **풀이 2**: 1씩 빼지 않고, N이 K로 나누어 떨어지는 수가 되도록 효율적으로 한번에 빼는 방법

```python
n, k = map(int, input().split())
result =  0

while True:
  # n이 k로 나누어 떨어지는 수가 될 때까지 1을 빼기 (1번)
  target = (n // k) * k # (n을 k로 나눈 몫) * k
  result += (n - target)
  n = target
  # n이 k보다 작아지면(나눌 수 없을 때) 반복문 탈출
  if n < k:
    break
  # n을 k로 나누기(2번)
  n //= k
  result += 1

# n이 k 미만이 되면 n=1이 될 때까지 1을 빼기
result += (n - 1)
print(result)
```