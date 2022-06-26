from collections import deque

# 도시 수, 도로 수, 최단 거리, 출발 도시 번호
n, m, k, x = map(int, input().split())

# 각 노드가 연결된 정보
graph = [[] for _ in range(n+1)] # 1~N번
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

# 모든 도시(노드)까지 걸리는 최단 거리 초기화
distance = [-1] * (n + 1)

# 최단 거리 함수
def bfs(graph, start):
  queue = deque([start]) # 큐 구현
  distance[start] = 0 # 자기 자신까지의 거리는 항상 0
  # 큐가 빌 때까지 반복
  while queue:
    now = queue.popleft()
    # 해당 도시(노드)와 인접하고 아직 방문하지 않은 원소들을 큐에 삽입
    for i in graph[now]:
      if distance[i] == -1:
        queue.append(i)
        distance[i] = distance[now] + 1 # 1씩 추가해서 최단거리 저장
  return distance

# 함수 실행
bfs(graph, x)

isExist = False # 최단 거리가 K인 도시 존재 여부
for i in range(1, n+1): # 1~N번까지의 도시 중에서
  if distance[i] == k: # 최단 거리가 K인 도시 출력
    print(i)
    isExist = True

# 최단 거리가 K인 도시가 없으면 -1 출력
if isExist == False:
  print(-1)
