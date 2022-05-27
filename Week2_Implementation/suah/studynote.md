## Implementation Algorithm
 
- 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정 
- 풀이를 떠올리는 것은 쉽지만 코드로 옮기기 어려움😭
- 예시 
  - 알고리즘은 간단한데 코드가 긴 문제 
  - 실수 연산 (특정 소수점까지 출력하는 문제) 
  - 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제 - python이 상대적으로 사용하기 쉬움
  - 적절한 라이브러리를 사용하는 문제 - ex) 순열&조합 찾는 문제 
- **완전 탐색** : 모든 경우의 수를 다 계산하는 해결 방법 
- **시뮬레이션** : 문제에서 제시한 알고리즘 한 단계씩 직접 수행
- 많은 연습이 필요함 
- 일반적으로 2차원 공간은 **행렬**의 의미로 사용됨 
- 시뮬레이션과 완전 탐색에서는 **방향벡터**가 자주 활용됨 
  ```python 
  # 동 북 서 남 
  dx = [0, -1, 0, 1]
  dy = [1, 0, -1, 0] 
  
  # 현재 위치 
  x, y = 2, 2
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx, ",", ny) 
    
  # 결과 
  # 2 , 3 / 1 , 2 / 2 , 1 / 3 , 2
  ```


</br>

*** 

### 예제 4-1번 - 상하좌우
```python
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
```

### 예제 4-2번 - 시각
```python
n = int(input())
answer = 0

for h in range(n + 1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                answer += 1

print(answer)
```

### 실전문제 - 왕실의 나이트 
```python 
now = input()
y = int(now[1])
x = ord(now[0]) - 96
count = 0

dx = [+1, +1, -1, -1, +2, +2, -2, -2]
dy = [+2, -2, +2, -2, -1, +1, -1, +1]
# steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

print(count)
```

### 실전문제 - 게임 개발 
```python 
import sys
input = lambda : sys.stdin.readline().strip()

n, m = map(int, input().split())
x, y, d = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[0] * m for _ in range(n)]
visited[x][y] = 1


def turn():
    global d
    d -= 1
    if d == -1:
        d = 3


turns = 0
count = 1
while True:
    turn()
    nx = x + dx[d]
    ny = y + dy[d]
    # 해당 위치가 육지이고 방문하지 않았을 경우
    if matrix[nx][ny] == 0 and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turns = 0
        continue
    else:
        turns += 1

    if turns == 4:   # 모든 방향으로 다 돌았을 경우
        nx = x - dx[d]
        ny = y - dy[d]
        if matrix[nx][ny] == 0:    # 뒤로 돌아갈 수 있는 경우
            x, y = nx, ny
        else:
            break
        turns = 0

print(count)
```
