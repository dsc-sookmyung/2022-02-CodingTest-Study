'''
Q.41) 여행 계획 

- n : 여행지 수 / m : 여행할 도시의 수 
- 순서에 맞게 여행을 할 수 있으면 YES 
- 여행 불가능하면 NO 
- 갔던 도시를 지나가는 것은 OK 
'''

import sys 
input = lambda : sys.stdin.readline().strip()

# 원소가 속한 집합 찾기 
def find_parent(parent, x):
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


n, m = map(int,input().split())
connect = [list(map(int, input().split())) for _ in range(n)]
city = list(map(int, input().split()))
parent = [0] * (n+1)

# 부모 테이블 자기 자신으로 초기화
for i in range(1, n+1):
	parent[i] = 1 

# 두 원소 이어져 있으면, 같이 속한 집합 찾기 
for j in range(0, n):
	for k in range(0, j):
		if connect[j][k] == 1:
			union_parent(parent, j+1, k+1)

# 가고자 하는 도시의 루트(연결 여부) 찾기
for c in range(len(city)): 
	city[c] = find_parent(parent, city[c])

if len(list(set(city))) == 1 : 
	print("YES")
else: 
	print("NO")
