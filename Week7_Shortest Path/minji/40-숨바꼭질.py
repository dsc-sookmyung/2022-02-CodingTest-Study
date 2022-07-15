import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) # 노드, 간선 수
graph = [[] for _ in range(n + 1)] # 각 노드의 연결 관계
distance = [INF] * (n + 1) # 최단 거리 테이블

# 노드 간 연결 관계
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append((b, 1)) # 모든 간선 길이는 1
  graph[b].append((a, 1)) # 양방향 간선이므로

# 다익스트라 알고리즘
def dijkstra(start):
  q = [(0, start)] # 시작 노드의 최단 거리 = 0
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

dijkstra(1)

max_node, max_dist = 0, 0 # 최단 거리가 가장 먼 노드 번호, 거리
result = [] # 동일한 거리를 가지는 노드 리스트
for i in range(1, n + 1):
  if max_dist < distance[i]:
    max_node = i
    max_dist = distance[i]
    result = [max_node]
  elif max_dist == distance[i]:
    result.append(i)

print(max_node, max_dist, len(result))