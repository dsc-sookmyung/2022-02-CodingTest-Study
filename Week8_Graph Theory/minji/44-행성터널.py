import heapq
import sys
input = sys.stdin.readline

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

n = int(input()) # 행성(노드) 개수
planets = [] # 모든 노드
parent = [i for i in range(n+1)] # 부모 테이블에서 부모를 자기 자신으로 초기화
result = 0 # 최종 비용

# 노드 정보
for i in range(n):
  x, y, z = map(int, input().split())
  planets.append((x, y, z, i))

# x, y, z 좌표에 대하여 오름차순 정렬
xsort = sorted(planets, key=lambda x: x[0])
ysort = sorted(planets, key=lambda x: x[1])
zsort = sorted(planets, key=lambda x: x[2])

q = [] # (간선 길이, 행성a, 행성b)
for i in range(n-1):
  heapq.heappush(q, (abs(xsort[i][0] - xsort[i+1][0]), xsort[i][3], xsort[i+1][3]))
  heapq.heappush(q, (abs(ysort[i][0] - ysort[i+1][0]), ysort[i][3], xsort[i+1][3]))
  heapq.heappush(q, (abs(zsort[i][0] - zsort[i+1][0]), zsort[i][3], xsort[i+1][3]))

# print(len(q))
for _ in range(n-1):
  cost, a, b = heapq.heappop(q)
  if find_parent(parent, a) != find_parent(parent, b): # 사이클이 발생하지 않는다면
    union_parent(parent, a, b) # 집합에 포함
    result += cost

print(result)