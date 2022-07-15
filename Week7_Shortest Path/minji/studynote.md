# 최단 경로

그래프 상에서 가장 짧은 경로를 찾는 알고리즘 (길 찾기 알고리즘)

## 다익스트라 알고리즘

특정한 노드에서 다른 모든 노드까지의 최단 경로 계산

- 음의 간선(0보다 작은 값인 간선)이 없다는 전제 하에 작동
- 기본적으로 그리디 알고리즘으로 분류: 매번 ‘가장 비용이 적은 노드’를 선택하기 때문
- 각 노드에 대한 현재까지의 최단 거리 정보를 항상 1차원 리스트에 저장, 갱신
- 이미 선택된 노드는 ‘최단 거리’가 완전히 선택되었으므로 값이 갱신되지 않음
    - 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것!
    - 즉 마지막 노드는 확인할 필요 X

**동작 과정**

1. 출발 노드 설정
2. 최단 거리 테이블을 무한(`int(1e9)`)으로 초기화
3. 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산, 더 작은 값이면 최단 거리 테이블 갱신
5. 3~4번 반복

**구현 방법**

(V=노드 개수, E=간선 개수)

1. 구현하기 쉽지만 느리게 동작하는 코드 - $O(V^2)$
    1. 최단 거리가 가장 짧은 노드를 찾기 위해 매번 최단 거리 테이블을 앞에서부터 하나씩 탐색
    2. V > 10,000일 경우 사용 불가
    
    ```python
    import sys
    
    input = sys.stdin.readline
    INF = int(1e9)
    
    n, m = map(int, input().split()) # 노드, 간선 수
    start = int(input()) # 시작 노드
    graph = [[] for _ in range(n + 1)] # 각 노드의 연결 관계 (인접 리스트)
    visited = [False] * (n + 1) # 방문 여부
    distance = [INF] * (n + 1) # 최단 거리 테이블
    
    # 노드 간 연결 관계
    for _ in range(m):
      a, b, c = map(int, input().split()) # a -> b 까지의 거리가 c
      graph[a].append((b, c))
    
    # 방문하지 않은 노드 중, 가장 최단 거리가 짧은 노드의 번호를 반환
    def get_smallest_node():
      min_value = INF
      index = 0 # 가장 최단 거리가 짧은 노드 번호
      for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
          min_value = distance[i]
          index = i
      return index
    
    # 다익스트라 알고리즘
    def dijkstra(start):
      distance[start] = 0 # 시작 노드의 최단 거리 = 0
      visited[start] = True
      for j in graph[start]:
        distance[j[0]] = j[1] # 다른 노드로 가는 거리 저장
      # 시작 노드 제외하고 n-1개의 노드에 대해 반복
      for i in range(n - 1):
        now = get_smallest_node() # 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드
        visited[now] = True
        # 현재 노드와 연결된 다른 노드들 확인
        for j in graph[now]:
          cost = distance[now] + j[1] # 현재 노드를 거쳐서 다른 노드로 가는 거리
          if cost < distance[j[0]]: # 최솟값이 되는 경우 최단 거리 테이블 업데이트
            distance[j[0]] = cost
    
    dijkstra(start)
    
    # 모든 노드로 가는 최단 거리
    for i in range(1, n + 1):
      if distance[i] == INF:
        print("INFINITY")
      else:
        print(distance[i])
    ```
    
2. 구현하기 까다롭지만 빠르게 동작하는 코드 - $O(ElogV)$
    1. 힙 자료구조 → 우선순위 큐 활용
    2. 최소 힙 이용하면 가장 값이 작은(=거리가 짧은) 원소가 나옴
    3. 우선순위 큐에서 꺼낸 노드가 이미 처리된 노드면 무시
    4. 방문 여부(visited), 최단 거리가 짧은 노드 찾는 함수(get_smallest_node) 불필요
    
    ```python
    import heapq
    import sys
    
    input = sys.stdin.readline
    INF = int(1e9)
    
    n, m = map(int, input().split()) # 노드, 간선 수
    start = int(input()) # 시작 노드
    graph = [[] for _ in range(n + 1)] # 각 노드의 연결 관계 (인접 리스트)
    distance = [INF] * (n + 1) # 최단 거리 테이블
    
    # 노드 간 연결 관계
    for _ in range(m):
      a, b, c = map(int, input().split()) # a -> b 까지의 거리가 c
      graph[a].append((b, c))
    
    # 다익스트라 알고리즘
    def dijkstra(start):
      q = []
      heapq.heappush(q, (0, start)) # 시작 노드의 최단 거리 = 0으로 설정하여 큐에 삽입
      distance[start] = 0 # 시작 노드의 최단 거리 = 0
      while q:
        dist, now = heapq.heappop(q) # 최단 거리가 가장 짧은 노드
        if distance[now] < dist: # 이미 처리되었다면 무시
          continue
        # 현재 노드와 연결된 다른 노드들 확인
        for i in graph[now]:
          cost = dist + i[1] # 현재 노드를 거쳐서 다른 노드로 가는 거리
          if cost < distance[i[0]]: # 최솟값이 되는 경우 최단 거리 테이블 업데이트
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0])) # 우선순위 큐에 추가
    
    dijkstra(start)
    
    # 모든 노드로 가는 최단 거리
    for i in range(1, n + 1):
      if distance[i] == INF:
        print("INFINITY")
      else:
        print(distance[i])
    ```
    

## 플로이드 워셜 알고리즘

모든 지점에서 다른 모든 지점까지의 최단 경로 계산

- 최단 거리 정보를 2차원 리스트에 저장
- 다이나믹 프로그래밍의 일종: 노드의 개수(N)만큼 점화식에 맞게 2차원 리스트 갱신
- 시간 복잡도 $O(N^3)$
- K번의 단계에 대한 점화식: $D_{ab} = min(D_{ab}, D_{ak}+D_{kb})$
    - A→B의 최소 거리와, A→K→B의 거리를 비교하여 더 작은 값으로 갱신

**동작 과정**

1. 2차원 테이블 초기화: 연결된 간선 (없으면 무한) 기입
    
    
    | 출발 \ 도착 | 1 | 2 | 3 | 4 |
    | --- | --- | --- | --- | --- |
    | 1 | 0 | 4 | 무한 | 6 |
    | 2 | 3 | 0 | 7 | 무한 |
    | 3 | 5 | 무한 | 0 | 4 |
    | 4 | 무한 | 무한 | 2 | 0 |
    1. 행=출발 노드, 열=도착 노드
    2. 자기 자신까지의 거리는 항상 0 → $D_{ii}$ = 0
2. 1~N번 노드를 거쳐가는 경우를 고려해서 더 작은 값으로 갱신

**구현 방법**

```python
INF = int(1e9)

# 노드, 간선 수
n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)] # 2차원 리스트 초기화

# 자기 자신까지의 거리는 0
for a in range(1, n + 1):
  for b in range(1, n + 1):
    if a == b:
      graph[a][b] = 0

# 노드 간 연결 관계
for _ in range(m):
  a, b, c = map(int, input().split()) # a -> b 까지의 거리가 c
  graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
  for b in range(1, n+1):
    if graph[a][b] == INF:
      print("INFINITY", end=" ")
    else:
      print(graph[a][b], end=" ")
  print()
```

### 정리

| 알고리즘 종류 | 시간 복잡도 | 구현 난이도 | 역할 |
| --- | --- | --- | --- |
| 다익스트라 | O(ElogV) | 어려운 편 | 한 지점에서 다른 모든 지점까지의 최단 경로 계산 |
| 플로이드 워셜 | O(V³) | 쉬운 편 | 모든 지점에서 다른 모든 지점까지의 최단 경로 계산 |

### 실전 1 - 미래 도시

- **문제**: 1 → K → X으로 가는 최소 거리는? (못 가면 -1)
    - 노드 개수=N, 간선 개수=M, 간선 길이=1, 양방향 통행 가능
- **풀이**: 플로이드 워셜 알고리즘: 1→K 최단 거리 + K→X 최단 거리
- **비고**: 1 ≤ N,M ≤ 100 ⇒ O(V³)

```python
INF = int(1e9)
n, m = map(int, input().split()) # 노드 수, 간선 수
graph = [[INF] * (n + 1) for _ in range(n + 1)] # 2차원 리스트 초기화

for a in range(1, n + 1):
  for b in range(1, n + 1):
    if a == b: # 자기 자신까지의 거리는 0
      graph[a][b] = 0

for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1 # 모든 간선 길이는 1
  graph[b][a] = 1 # 양방향 간선이므로

x, k = map(int, input().split()) # 목적지, 경유지

# 플로이드 워셜 알고리즘
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]
if distance >= INF:
  print("-1")
else:
  print(distance)
```

### 실전 2 - 전보

- **문제**: 도시 C에서 보낸 메시지를 받을 수 있는 도시의 개수, 모두 받는데 걸리는 시간은?
    - 양방향 통로가 있어야 전송 가능
- **풀이**: 다익스트라 알고리즘
    - 모두 받는데 걸리는 시간=최단 거리들 중 최댓값 (무한 제외)
- **비고**: 1≤도시 개수 N ≤3만, 1≤통로 개수 M≤20만, 1≤C≤M

```python
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split()) # 노드 수, 간선 수, 목적지 노드
graph = [[] for _ in range(n + 1)] # 각 노드의 연결 관계 (인접 리스트)
distance = [INF] * (n + 1) # 최단 거리 테이블

for _ in range(m):
  x, y, z = map(int, input().split()) # x -> y 까지의 거리가 z
  graph[x].append((y, z))

# 다익스트라 알고리즘
def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start)) # 시작 노드의 최단 거리 = 0
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q) # 최단 거리가 가장 짧은 노드
    if distance[now] < dist: # 이미 처리되었다면 무시
      continue
    # 현재 노드와 연결된 다른 노드들 확인
    for i in graph[now]:
      cost = dist + i[1] # 현재 노드를 거쳐서 다른 노드로 가는 거리
      if cost < distance[i[0]]: # 최솟값이 되는 경우 최단 거리 테이블 업데이트
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0])) # 우선순위 큐에 추가

dijkstra(c)

city, time = 0, 0
for i in distance:
  if i != INF:
    city += 1
    time = max(time, i) # 최단 거리들 중 최댓값

print(city-1, time) # 시작 노드는 제외하므로 city-1
```