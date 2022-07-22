# 그래프 이론

### 그래프와 트리의 차이점

|  | 그래프 | 트리 |
| --- | --- | --- |
| 방향성 | 방향 또는 무방향 | 방향 |
| 순환성 | 순환 및 비순환 | 비순환 |
| 루트 노드 존재 여부 | X | O |
| 노드 간 관계성 | 부모와 자식 관계 X | 부모와 자식 관계 |
| 모델의 종류 | 네트워크 모델 | 계층 모델 |

### 그래프 구현 방법 (복습)

(노드 개수=V, 간선 개수=E)

- 인접 행렬: 2차원 배열
    - 메모리 공간: $O(V^2)$
    - 특정한 노드 A에서 노드 B로 이어진 간선의 비용을 파악하는 시간: $O(1)$
    - 활용 사례: 플로이드 워셜 알고리즘
- 인접 리스트: 리스트
    - 메모리 공간: $O(E)$
    - 특정한 노드 A에서 노드 B로 이어진 간선의 비용을 파악하는 시간: $O(V)$
    - 활용 사례: 다익스트라 최단 경로 알고리즘

<br/>

## 서로소 집합 자료구조

서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조

- 서로소 집합: 공통 원소가 없는 두 집합
    - {1, 2}와 {3, 4}는 서로소 관계
    - {1, 2}와 {2, 3}은 서로소 관계가 아님
- 연산
    - **union**(합집합): 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
    - **find**(찾기): 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산
- 트리 자료구조를 이용

**서로소 집합 정보(합집합 연산)가 주어졌을 때의 계산 원리**

1. union(합집합) 연산을 확인하여, 서로 연결된 두 원소(노드) A, B를 확인
    1. A와 B의 루트 노드 A’, B’를 각각 찾음
    2. A’를 B’의 부모 노드로 설정 (B’가 A’를 가리킴)
    (실제로는 번호가 더 작은 원소가 부모 노드가 되도록 구현)
2. 모든 union(합집합) 연산을 처리할 때까지 1번 과정 반복

ex) union 1, 4 / union 2, 3 / union 2, 4 / union 5, 6

![image](https://user-images.githubusercontent.com/61882016/180393142-dcdc5cf6-8c1d-43cc-9f7f-ef92c90113a0.png)

- 자식(큰 수) 노드가 부모(작은 수) 노드를 가리키는 트리 자료구조
- 원소=노드, union 연산=간선 ⇒ 6개의 노드, 4개의 간선으로 이루어진 그래프로도 표현 가능
- {1, 2, 3, 4} / {5, 6}으로 나누어짐

**알고리즘 동작 과정**

1. 노드 개수(V) 크기의 부모 테이블을 초기화
    1. 모든 원소가 자기 자신을 부모로 가지도록 설정
    2. 부모 테이블은 오직 부모에 대한 정보만 담고 있음
2. union 연산으로 더 큰 루트 노드가 더 작은 루트 노드를 가리키도록 설정
    1. union 1, 4 : 노드 4의 부모를 1로 설정
    2. union 2, 3 : 노드 3의 부모를 2로 설정
    3. union 2, 4 : 노드 2의 부모를 1로 설정
    4. union 5, 6 : 노드 6의 부모를 5로 설정
- 루트 노드를 찾으려면 재귀적으로 부모를 거슬러 올라가야 함
- 노드 3의 최종적인 루트 노드 = 노드 1

```python
# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
  # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
  if parent[x] != x:
    return find_parent(parent, parent[x])
  return x

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# 노드 개수, 간선(union 연산) 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블

# 부모 테이블에서 부모를 자기 자신으로 초기화
for i in range(1, v+1):
  parent[i] = i

# union 연산 수행
for i in range(e):
  a, b = map(int, input().split())
  union_parent(parent, a, b)

print('각 원소가 속한 집합(각 원소의 루트 노드): ', end='')
for i in range(1, v+1):
  print(find_parent(parent, i), end=' ') # 1 1 1 1 5 5
print()

print('부모 테이블: ', end='')
for i in range(1, v+1):
  print(parent[i], end=' ') # 1 1 2 1 5 5
```

- find 함수의 시간 복잡도 = $O(V)$ ⇒ 연산 개수가 M개일 때 전체 시간 복잡도 = $O(VM)$으로 비효율적
- 경로 압축: find 함수를 재귀적으로 호출하고 부모 테이블 값 갱신하여 최적화

```python
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]
```

### 시간 복잡도

노드 개수=V, 최대 V-1개의 union 연산과 M개의 find 연산이 가능하다고 가정

⇒ $O(V+M(1+log_{2-M/V}V))$

ex) 1000개 노드, 연산 100만 번 ⇒ 약 1000만 번 연산 필요

### 사이클 판별

무방향 그래프 내에서의 사이클 여부 판별

1. 각 간선을 확인, 두 노드의 루트 노드를 확인
    1. 서로 다르면 두 노드에 대해 union 연산
    2. 서로 같으면 사이클 발생한 것임
2. 그래프에 포함된 모든 간선에 대하여 1번 과정 반복

```python
# find/union 함수, 입력받기, 부모 테이블(parent) 초기화는 위와 동일
cycle = False # 사이클 발생 여부

for i in range(e):
  a, b = map(int, input().split())
  if find_parent(parent, a) == find_parent(parent, b):
    cycle = True
    break
  else:
    union_parent(parent, a, b)
```
<br/>

## 신장 트리(Spanning Tree)

하나의 그래프가 있을 때, 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프

![image](https://user-images.githubusercontent.com/61882016/180393205-f6e90fc0-bd13-4438-b8a4-eb3ac8f7e64f.png)

### 크루스칼(Kruskal)

- 최소한의 비용으로 신장 트리를 찾는 최소 신장 트리 알고리즘의 대표 사례
    - ex) N개 도시가 존재할 때, 두 도시 사이에 도로를 놓아 전체 도시가 연결되도록 함
    - 도시 A에서 B로 이동하는 경로가 반드시 존재하도록 도로 설치
    - 모든 도시를 ‘연결’할 때, 최소한의 비용으로 연결하려면?
- 그리디 알고리즘으로 분류
    - 모든 간선에 대하여 정렬 수행 → 가장 거리가 짧은 간선부터 집합에 포함
    - 사이클을 발생시킬 수 있는 간선은 포함 X

**실행 원리**

1. 간선 데이터를 비용에 따라 오름차순 정렬
2. 간선을 하나씩 확인하며 현재의 간선이 사이클 발생시키는지 확인
    1. 사이클 발생 X ⇒ 최소 신장 트리에 포함
    2. 사이클 발생 ⇒ 포함 X
3. 모든 간선에 대하여 2번 과정 반복 ⇒ 신장 트리에 포함되는 간선 개수 = 노드 개수 - 1

**알고리즘 동작 과정**

1. 그래프의 모든 간선 정보만 따로 빼서 정렬
2. 가장 짧은 간선 선택, 집합에 포함 = 두 노드를 union 연산
    1. 해당 노드의 루트가 이미 동일한 집합에 포함되어 있으면 제외

```python
# find/union 함수, 입력받기, 부모 테이블(parent) 초기화는 위와 동일
edges = [] # 모든 간선
result = 0 # 최종 비용

for _ in range(e):
  a, b, cost = map(int, input().split()) # 노드와 간선 정보
  edges.append((cost, a, b))

edges.sort() # 간선을 비용 순으로 정렬

for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b): # 사이클이 발생하지 않는다면
    union_parent(parent, a, b) # 집합에 포함
    result += cost

print(result)
```

### 시간 복잡도

간선 개수=E일 때 ⇒ $O(ElogE)$

- =E개의 데이터를 정렬했을 때 시간 복잡도
- 크루스칼 내부의 서로소 집합 알고리즘의 시간 복잡도는 더 작으므로 무시

<br/>

## 위상 정렬(Topology)

방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열

- 정렬 알고리즘의 일종
    - ex) 순서가 정해진 일련의 작업을 차례대로 수행할 때 사용
    - 선수과목을 고려한 학습 순서 설정
- 큐 또는 스택 자료구조 활용
- 진입차수(Indegree): 특정 노드로 들어오는 간선의 개수

![image](https://user-images.githubusercontent.com/61882016/180393240-96599f4b-47dc-4310-b075-12cdae2b1fba.png)
1-2-5-3-6-4-7 또는 1-5-2-3-6-4-7 (큐에서 꺼내는 순서에 따라)

**실행 원리**

1. 진입차수=0인 노드를 큐에 삽입
2. 큐가 빌 때까지 다음의 과정 반복
    1. 큐에서 원소를 꺼내, 해당 노드에서 출발하는 간선을 그래프에서 제거
    2. 새롭게 진입차수가 0이 된 노드를 큐에 삽입
- 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 발생한 것 (보통 사이클이 발생하지 않는다는 전제)

**알고리즘 동작 과정**

```python
from collections import deque

v, e = map(int, input().split()) # 노드 개수, 간선 개수
indegree = [0] * (v+1) # 모든 노드에 대한 진입차수
graph = [[] for _ in range(v+1)] # 각 노드에 연결된 간선 정보

# 각 노드에 연결된 간선 정보
for _ in range(e):
  a, b = map(int, input().split()) # a -> b
  graph[a].append(b)
  indegree[b] += 1 # 진입차수 1 증가

# 위상 정렬 함수
def topology_sort():
  result = []
  q = deque()

  # 진입차수가 0인 노드를 큐에 삽입
  for i in range(1, v+1):
    if indegree[i] == 0:
      q.append(i)
  
  # 큐가 빌 때까지 반복
  while q:
    now = q.popleft() # 큐에서 원소 꺼내기
    result.append(now)
    # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
    for i in graph[now]:
      indegree[i] -= 1
      # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
      if indegree[i] == 0:
        q.append(i)
  
  # 수행 결과
  for i in result:
    print(i, end=' ')

topology_sort()
```

### 시간 복잡도

노드 개수=V, 간선 개수=E일 때 ⇒ $O(V+E)$

- 모든 노드를 차례대로 확인하면서, 해당 노드에서 출발하는 간선을 차례대로 제거하므로