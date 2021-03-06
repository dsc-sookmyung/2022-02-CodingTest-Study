# 다이나믹 프로그래밍

한 번 해결된 부분 문제의 정답을 메모리에 기록하여, 한 번 계산된 답은 다시 계산하지 않도록 하는 알고리즘

- 점화식(인접한 항들 사이의 관계식) 이용
- 메모리 공간을 약간 더 사용하여 연산 속도 증가

**사용 조건**

1. 큰 문제를 작은 문제로 나눌 수 있을 때
2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일할 때

### 코드 작성법

1. 탑다운(Top-Down)
    - 재귀 함수 이용
    - 큰 문제를 해결하기 위해 작은 문제 호출
2. 보텀업(Bottom-Up)
    - 단순 반복문 이용
    - 작은 문제 먼저 해결, 해결된 작은 문제를 모아 큰 문제 해결
    - 권장하는 방법

### 예제 - 피보나치 수열

$a_{n+2} = a_{n+1} + a_{n} (a_1=1, a_2=1)$

한 번 계산한 i번째 피보나치 수를 모두 1차원 리스트에 저장

- 풀이 1: 재귀 함수로 구현
    - 시간 복잡도 $O(2^N)$ ⇒ n이 커지면 수행 시간이 너무 커지는 문제
    
    ```python
    def fibo(x):
    	if x == 1 or x == 2:
    		return 1
    	return fibo(x-1) + fibo(x-2)
    ```
    
- 풀이 2: 다이나믹 프로그래밍 - 메모이제이션 기법 활용 (**탑다운** 방식)
    - 메모이제이션(Memoization) 기법: 한 번 구한 결과를 메모리 공간에 저장 = 캐싱(Caching)
    - 시간 복잡도 $O(N)$
    
    ```python
    # 한 번 계산된 결과를 메모이제이션하기 위한 리스트
    d = [0] * 100
    
    def fibo(x):
    	if x == 1 or x == 2:
    		return 1
    	# 이미 계산한 적 있는 문제라면 그대로 반환
    	if d[x] != 0:
    		return d[x]
    	# 아직 계산하지 않은 문제라면 피보나치 결과 저장
    	d[x] = fibo(x-1) + fibo(x-2)
    	return d[x]
    ```
    
- 풀이 3: 반복문 활용 (**보텀업** 방식)
    
    ```python
    # 한 번 계산된 결과를 저장하기 위한 DP 테이블
    d = [0] * 100
    
    d[1] = 1
    d[2] = 1
    n = 99
    
    for i in range(3, n+1):
    	d[i] = d[i-1] + d[i-2]
    
    print(d[n])
    ```
    

### 실전 1 - 1로 만들기

- **문제**: 정수 X가 주어졌을 때 연산 4개를 사용해서 1로 만드는데, 연산 횟수의 최솟값은?
    1. 5로 나누어 떨어지면 5로 나누기
    2. 3로 나누어 떨어지면 3으로 나누기
    3. 2로 나누어 떨어지면 2로 나누기
    4. 1을 빼기
- **풀이**: 보텀업 다이나믹 프로그래밍
    - 점화식: $a_i = min(a_{i-1}, a_{i/2}, a_{i/3}, a_{i/5}) + 1$
    - 1을 더하는 이유: 함수의 호출 횟수 구하기 위해
- **비고**: 1 ≤ X ≤ 30000

```python
x = int(input())
d = [0] * 30001 # 결과 저장

# 보텀업 다이나믹 프로그래밍
for i in range(2, x+1):
  d[i] = d[i-1] + 1 # 현재의 수에서 1을 빼는 경우
  if i % 2 == 0: # 2로 나누어 떨어질 때
    d[i] = min(d[i], d[i//2] + 1)
  if i % 3 == 0: # 3으로 나누어 떨어질 때
    d[i] = min(d[i], d[i//3] + 1)
  if i % 5 == 0: # 5로 나누어 떨어질 때
    d[i] = min(d[i], d[i//5] + 1)

print(d[x])
```

### 실전 2 - 개미 전사

- **문제**: N개의 식량 창고에서 얻을 수 있는 식량(숫자)의 최댓값은? (인접한 식량 창고는 약탈할 수 없음)
- **풀이:** 보텀업 다이나믹 프로그래밍
    - 왼쪽부터 차례대로 창고를 털지 안 털지를 결정
    - i번째 창고 약탈 가능 여부를 결정 (a와 b 중 큰 값 선택)
        1. (i-1)번째 창고를 털면 i번째 창고를 털 수 없음
        2. (i-2)번째 창고를 털면 i번째 창고를 털 수 있음
    - 점화식: $a_i = max(a_{i-1}, a_{i-2} + k_i)$
        - $k_i$: i번째 식량창고에 있는 식량의 양
- **비고**: 3 ≤ n ≤ 100

```python
n = int(input())
array  = list(map(int, input().split()))
d = [0] * 100

# 보텀업 다이나믹 프로그래밍
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
  d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1])
```

### 실전 3 - 바닥 공사

- **문제**: 가로 N, 세로 2인 직사각형을 1*2, 2*1, 2*2의 덮개로 채우는 모든 경우의 수 /  796,796
- **풀이**: 왼쪽부터 차례대로 채운다면
    - (i-1)까지 채워졌을 때: 2*1 1개 - 1가지
    - (i-2)까지 채워졌을 때: 1*2 2개 / 2*2 1개 - 2가지
    - 점화식: $a_i = a_{i-1} + a_{i-2} * 2$
- **비고**:

```python
n = int(input())
d = [0] * 1001

# 보텀업 다이나믹 프로그래밍
d[1] = 1
d[2] = 3
for i in range(3, n):
  d[i] = (d[i-1] + d[i-2] * 2) % 796796

print(d[n])
```

### 실전 4 - 효율적인 화폐 구성

- **문제**: N가지 종류의 화폐로 M원을 만들기 위한 화폐 개수의 최솟값 (불가능할 때는 -1)
- **풀이**: $a_i$ = 금액 i를 만들 수 있는 최소한의 화폐 수, k = 화폐의 단위
    - $a_{i-k}$를 만드는 방법 존재 → $a_i=min(a_i, a_{i-k}+1)$
    - $a_{i-k}$를 만드는 방법 없음 → $a_i=10,001$
        - 왜 10001이냐? → M의 최대 크기가 10000이라서
    - $a_0$ = 0 (0원을 만드는 화폐 수는 0이므로)
- **비고**: 1 ≤ N ≤ 100, 1 ≤ M ≤ 10000
    - 그리디 알고리즘 예제 1 (거스름돈)과 유사하나, 큰 단위가 작은 단위의 배수가 아님

```python
n, m = map(int, input().split()) # 화폐 종류 수, 목표 금액
coin_types = [] # 화폐 종류
for _ in range(n):
  coin_types.append(int(input()))

d = [10001] * (m + 1) # 한 번 계산한 결과를 저장할 DP 테이블
d[0] = 0

# 보텀업 다이나믹 프로그래밍
for coin in coin_types:
  for i in range(coin, m + 1):
    d[i] = min(d[i], d[i - coin] + 1)

if d[m] == 10001: # m원을 만드는 방법이 없을 때
  print(-1)
else:
  print(d[m])
```