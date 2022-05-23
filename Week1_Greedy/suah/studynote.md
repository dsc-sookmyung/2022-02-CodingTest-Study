## Greedy Algorithm 

- 현재 상황에서 지금 당장 좋은 것만 고르는 방법 
- 매 순간 가장 좋은 것만 선택하고 이후에 미칠 영향은 고려하지 X 
- 창의력(문제를 풀 수 있는 아이디어) 필요 
- 정렬 알고리즘과 짝을 이뤄 같이 출제되는 경향 O
- **정당성 분석**이 중요 
  - 단순히 가장 좋아 보이는 것을 반복적으로 선택해도 최적의 해를 구할 수 있는가? 
- 문제 유형을 바로 파악하기 어렵다면 Greedy 의심해보기!  


</br>

*** 

### 실전문제 1번 - 큰 수의 법칙 
```python
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

arr.sort()
while m > 0:
    for _ in range(k):
        if m == 0:
            break
        answer += arr[n-1]
        m -= 1
    if m == 0:
        break
    answer += arr[n-2]
    m -= 1

print(answer)
```

### 실전문제 2번 - 숫자 카드 게임 
```python
N, M = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(N)]
maxx = 0

for i in range(N):
    temp = min(cards[i])
    if temp > maxx:
        maxx = temp

print(maxx)
```

### 실전문제 3번 - 1이 될 때까지 
```python
n, k = map(int, input().split())
count = 0

while n >= 1:
    if n == 1 :
        break
    elif n % k == 0:
        n = n // k
        count += 1
    else :
        n = n-1
        count += 1

print(count)
```
