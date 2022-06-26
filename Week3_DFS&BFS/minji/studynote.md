# 탐색

많은 양의 데이터 중에서 원하는 데이터를 찾는 과정

- 프로그래밍에서는 그래프, 트리 등의 자료구조 안에서 탐색하는 문제를 자주 다룸
- 대표적인 탐색 알고리즘: DFS, BFS

## 선행 개념

### 1. 자료구조

데이터를 표현, 관리, 처리하기 위한 구조

**스택, 큐를 이루는 핵심 개념**

- push: 데이터 삽입
- pop: 데이터 삭제
- 오버플로(Overflow): 특정 자료구조가 수용할 수 있는 데이터의 크기를 이미 가득 찬 상태에서 삽입 연산을 수행할 때 발생
- 언더플로(Underflow): 데이터가 없는 상태에서 삭제 연산을 수행할 때 발생

#### 1-1. 스택(Stack)

선입후출(First In Last Out) 구조

- append(): 데이터 삽입
- pop(): 데이터 삭제

```python
stack = []

stack.append(5)
stack.append(2)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력
```

#### 1-2. 큐(Queue)

선입선출(First In First Out) 구조

- collections 모듈에서 제공하는 deque 자료구조 활용
    - 스택과 큐의 장점을 모두 채택
    - 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적
    - queue 라이브러리보다 더 간단
- append(): 데이터 삽입
- popleft(): 데이터 삭제

```python
from collections import deque

queue = deque() # deque 라이브러리 사용하여 Queue 구현

queue.append(5)
queue.append(2)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력
```

### 2. 재귀 함수 (Recursive Function)

자기 자신을 다시 호출하는 함수

※ 파이썬 인터프리터에서는 재귀 호출 횟수 제한 있음

**재귀 함수 종료 조건**

- **목적**: 재귀 함수 무한 호출 방지

```python
def recursive_function(i):
  if i == 5:
    return
  print(i, '번째 재귀 함수에서', i + 1, '번째 재귀 함수를 호출')
  recursive_function(i + 1)
  print(i, '번째 재귀 함수 종료')

recursive_function(1)
```

```python
1 번째 재귀 함수에서 2 번째 재귀 함수를 호출
2 번째 재귀 함수에서 3 번째 재귀 함수를 호출
3 번째 재귀 함수에서 4 번째 재귀 함수를 호출
4 번째 재귀 함수에서 5 번째 재귀 함수를 호출
4 번째 재귀 함수 종료
3 번째 재귀 함수 종료
2 번째 재귀 함수 종료
1 번째 재귀 함수 종료
```

- 스택 자료구조 이용하여 수행: 가장 마지막에 호출한 함수가 먼저 수행을 끝내야 그 앞의 함수 호출이 종료
- ⇒ 스택 자료구조를 활용해야 하는 상당수 알고리즘은 재귀 함수를 통해 구현 가능
    - 예) DFS

- **대표적인 사례**: 팩토리얼
    - n ≤ 1 ⇒ n! = 1
        
        ![증명](https://user-images.githubusercontent.com/61882016/175568039-e769ee2f-147a-48d8-9f17-351a6c88c17e.png)
        증명
        
    - n > 1 ⇒ n! = n * (n-1)! 임을 활용
    
    ```python
    def factorial(n):
      if n <= 1:
        return 1
      return n * factorial(n - 1)
    
    print(factorial(5))
    ```
    

- **장점**
    - 코드가 더 간결: 수학의 점화식(재귀식)을 구현해 놓았기 때문
        - 점화식: 특정한 함수를 자신보다 더 작은 변수에 대한 함수와의 관계로 표현한 것
        - 다이나믹 프로그래밍에서 적용되는 중요한 개념

### 그래프

![image](https://user-images.githubusercontent.com/61882016/175567948-84399843-c983-487d-ba19-a48085fa6f85.png)

- 노드(node) = 정점(vertex): 위치
- 간선(edge): 노드를 연결하는 선. 노드 간의 관계
- 그래프 탐색: 하나의 노드를 시작으로 다수의 노드를 방문
- 인접한 노드(adjacent): 두 노드가 간선으로 연결되어 있을 때

**그래프의 연결 관계를 표현하는 방법**

![image](https://user-images.githubusercontent.com/61882016/175568297-796a4095-9fcc-4e7d-aaf2-b77520f3e24d.png)

(사진 출처: [Velog](https://velog.io/@hyesoup/%EC%9D%B4%EA%B2%83%EC%9D%B4-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4-DFSBFS-6a42zof2))

1. **인접 행렬**(Adjacency Matrix): 2차원 배열(Python에서는 리스트)에 각 노드가 연결된 형태를 기록
    
    * 연결되지 않은 노드끼리는 무한으로 표현
    
    - 메모리: 모든 관계를 저장 ⇒ 노드 개수가 많을 수록 메모리를 불필요하게 낭비
    - 속도: 특정한 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도가 빠름
        - 노드 1과 노드 7의 연결 여부: graph[1][7]
    
    ```python
    INF = 999999999
    
    graph = [
      [0, 3, 6],
      [3, 0, INF],
      [6, INF, 0]
    ]
    
    print(graph)
    ```
    
2. **인접 리스트**(Adjacency List): 모든 노드에 연결된 노드에 대한 정보(노드, 거리)를 차례대로 연결하여 저장
    - 메모리: 연결된 정보만을 저장 ⇒ 메모리를 효율적으로 사용
        - 특정 노드와 연결된 모든 인접 노드를 순회해야 하는 경우, 인접 행렬 방식보다 메모리 공간의 낭비가 적음
    - 속도: 특정한 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도가 느림
        - 노드 1과 노드 7의 연결 여부: 노드 1의 인접 리스트를 차례대로 확인해야 함
    
    ```python
    graph = [[] for _ in range(3)]
    
    graph[0].append((1, 3))
    graph[0].append((2, 6))
    
    graph[1].append((0, 3))
    
    graph[2].append((0, 6))
    
    print(graph) # [[(1, 3), (2, 6)], [(0, 3)], [(0, 6)]]
    ```
    

## DFS (Depth-First Search)

깊이 우선 탐색: 그래프에서 깊은 부분을 우선적으로 탐색

- 스택 자료구조 이용 (실제로는 재귀 함수 활용)
- 방문 처리: 스택에 한 번 삽입되어 처리된 노드가 다시 삽입되지 않게 체크하는 것
- 백트래킹(Backtracking): 한 방향으로 들어갔다가 막다른 길에 다다르면(=트리의 바닥에 도착) 왔던 길을 돌아가서 다른 방향으로 가는 것
- 데이터의 개수가 N개 ⇒ 시간 복잡도 $O(N)$

![dfs](https://user-images.githubusercontent.com/61882016/175568716-272fc88b-8f76-4125-a3b5-9063879ad648.gif)

[https://www.codesdope.com/course/algorithms-dfs/](https://www.codesdope.com/course/algorithms-dfs/)

1. 탐색 시작 노드를 스택에 삽입, 방문 처리
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리, 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복

```python
def dfs(graph, v, visited):
  # 현재 노드를 방문 처리
  visited[v] = True
  print(v, end=' ')
  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

# 각 노드가 연결된 정보 (142p)
graph = [
  [], # 0번 노드는 없으므로
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보
visited = [False] * 9

# dfs 함수 호출
dfs(graph, 1, visited) # 1 2 7 6 8 3 4 5
```

## BFS

너비 우선 탐색: 가까운 노드부터 우선적으로 탐색

- 큐 자료구조 이용
- 데이터의 개수가 N개 ⇒ 시간 복잡도 $O(N)$
- 실제 수행 시간은 DFS보다 더 빠름

![bfs](https://user-images.githubusercontent.com/61882016/175568712-2349e8d0-fdc8-4859-8814-a6ec63f324fb.gif)

[https://victorqi.gitbooks.io/swift-algorithm/content/breadth-first_search_bfs.html](https://victorqi.gitbooks.io/swift-algorithm/content/breadth-first_search_bfs.html)

1. 탐색 시작 노드를 스택에 삽입, 방문 처리
2. 큐에서 노드를 꺼내, 해당 노드의 인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입, 방문 처리
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복

```python
from collections import deque

def bfs(graph, start, visited):
  queue = deque([start]) # 큐 구현
  # 현재 노드를 방문 처리
  visited[start] = True
  # 큐가 빌 때까지 반복
  while queue:
    # 큐에서 하나의 원소를 뽑아 출력
    v = queue.popleft()
    print(v, end=' ')
    # 해당 노드와 인접하고 아직 방문하지 않은 원소들을 큐에 삽입, 방문 처리
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

# 각 노드가 연결된 정보 (142p)
graph = [
  [], # 0번 노드는 없으므로
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보
visited = [False] * 9

# bfs 함수 호출
bfs(graph, 1, visited) # 1 2 3 8 7 4 5 6
```

<aside>
💡 2차원 배열에서의 탐색 문제 ⇒ 그래프로 바꾸어 표현 ⇒ DFS 또는 BFS 활용
</aside>

### 실전 1 - 음료수 얼려 먹기

- **문제**: n * m 크기의 얼음 틀 모양이 주어졌을 때, 생성되는 총 아이스크림의 개수
    - 구멍 뚫린 부분=0, 칸막이=1
    - 구멍이 뚫린 부분끼리 상하좌우로 붙어있는 경우 연결되어 있다고 간주
- **풀이**: DFS - 0인 값이 연결되어 있는 노드 묶음 찾기
    1. 특정 노드의 주변에서 값=0이면서 아직 방문하지 않은 노드가 있다면 해당 노드를 방문
    2. 방문한 노드에서 다시 주변 노드 찾아서 방문
    3. 1~2번 과정을 모든 노드에 반복하며 방문하지 않은 지점의 수를 셈

```python
n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input())))

def dfs(x, y):
  # 주어진 범위를 벗어나는 경우 종료
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  # 현재 노드를 방문하지 않았다면
  if graph[x][y] == 0:
    graph[x][y] = 1 # 방문 처리
    # 현재 노드와 연결된(상하좌우) 다른 노드를 재귀적으로 방문
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True # 한 묶음을 True 처리
  return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
  for j in range(m):
    # 현재 위치에서 dfs 수행
    if dfs(i, j) == True:
      result += 1

print(result)
```

### 실전 2 - 미로 탈출

- **문제**: n * m 크기 미로에서 탈출하기 위해 움직여야 하는 최소 칸 수
    - 최초 위치=(1, 1), 미로 출구=(n, m)
    - 괴물 있는 곳=0, 괴물 없는 곳=1
    - 시작 칸과 마지막 칸은 반드시 1
- **풀이**: BFS - 시작 노드에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색
    - 특정한 노드를 방문하면, 그 이전 노드의 거리에 1을 더한 값을 저장

```python
from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input())))

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  queue = deque() # 큐 구현
  queue.append((x, y))
  # 큐가 빌 때까지 반복
  while queue:
    x, y = queue.popleft()
    # 현재 위치에서 상하좌우 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 공간을 벗어난 경우 무시
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      # 괴물이 있는 곳일 경우 무시
      if graph[nx][ny] == 0:
        continue
      # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  # 가장 오른쪽 아래까지의 최단 거리 반환
  return graph[n-1][m-1]

print(bfs(0, 0))
```
