import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

t = int(input()) # 테스트 케이스
for _ in range(t):
  n = int(input()) # 맵 크기
  graph = [] # 맵 정보
  for _ in range(n):
    graph.append(list(map(int, input().split())))

  distance = [[INF] * n for _ in range(n)] # 최단 거리 테이블
  x, y = 0, 0 # 시작 위치 (0, 0)
  q = [(graph[x][y], x, y)]
  distance[x][y] = graph[x][y]
  
  while q:
    dist, x, y = heapq.heappop(q) # 최단 거리가 가장 짧은 노드
    if distance[x][y] < dist: # 이미 처리되었다면 무시
      continue
    for i in range(4): # 인접 노드 확인
      nx = x + dx[i]
      ny = y + dy[i]
      # 공간 벗어나면 무시
      if nx < 0 or ny < 0 or nx >= n or ny >= n:
        continue
      cost = dist + graph[nx][ny] # 현재 노드를 거쳐서 다른 노드로 가는 거리
      if cost < distance[nx][ny]: # 최솟값이 되는 경우 최단 거리 테이블 업데이트
        distance[nx][ny] = cost
        heapq.heappush(q, (cost, nx, ny)) # 우선순위 큐에 추가
        
  print(distance[n-1][n-1])