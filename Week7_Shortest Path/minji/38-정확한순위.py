INF = int(1e9)

n, m = map(int, input().split()) # 학생 수, 비교 횟수
graph = [[INF] * (n + 1) for _ in range(n + 1)] # 2차원 리스트 초기화

# 자기 자신까지의 거리는 0
for a in range(1, n + 1):
  for b in range(1, n + 1):
    if a == b:
      graph[a][b] = 0

# 노드 간 연결 관계
for _ in range(m):
  a, b = map(int, input().split()) # a < b
  graph[a][b] = 1 # 간선의 거리는 1

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0

# 각 학생을 번호에 따라 한 명씩 확인하며 도달 가능한지 체크
for i in range(1, n + 1) :
  count = 0
  for j in range(1, n + 1) :
    if graph[i][j] != INF or graph[j][i] != INF :
      count += 1

  if count == n : # n개의 노드 모두 도달 가능하다면
    result += 1

print(result)