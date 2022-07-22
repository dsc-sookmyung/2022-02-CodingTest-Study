INF = int(1e9)

n = int(input()) # 노드 수
m = int(input()) # 간선 수
graph = [[INF] * (n+1) for _ in range(n+1)] # 2차원 리스트 초기화

# 자기 자신까지의 거리는 0
for a in range(1, n+1):
  for b in range(1, n+1):
    if a == b:
      graph[a][b] = 0

# 노드 간 연결 관계
for _ in range(m):
  a, b, c = map(int, input().split()) # a -> b 까지의 거리가 c
  if c < graph[a][b]: # 가장 짧은 간선만 저장
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
  for b in range(1, n+1):
    if graph[a][b] == INF:
      print(0, end=" ")
    else:
      print(graph[a][b], end=" ")
  print()