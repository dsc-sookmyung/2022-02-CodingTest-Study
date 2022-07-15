'''
Q39. 화성 탐사 

<문제> 
- [0][0]에서 [N-1][N-1]까지의 최적의 경로(최소 비용) 
- 상하좌우 1칸씩 이동 가능 
'''

'''
¿heapq?

이진트리 기반의 min heap 자료구조 제공. 
≈ 우선순위큐
항상 작은 값은 루트에 위치함. 
'''

import sys
import heapq
input = lambda : sys.stdin.readline().strip()

t = int(input())

for _ in range(t):
    # 탐사 공간
    n = int(input())
    # 탐사 공간에 대한 비용
    graph = []

    for i in range(n):
        graph.append(list(map(int, input().split())))
    
    # 다익스트라를 위한 q
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    
    # 상하좌우 탐색을 위한 ds
    ds = ((0, 1), (0, -1), (1, 0), (-1, 0))

    distance = [[1e9] * n for _ in range(n)]
    distance[0][0] = graph[0][0]

    while q:
        # heappop은 가장 작은 원소 반환
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue

        for d in ds:
            dx = x + d[0]
            dy = y + d[1]

            if 0 <= dx and dx < n and 0 <= dy and dy < n:
                cost = dist + graph[dx][dy]

                if cost < distance[dx][dy]:
                    distance[dx][dy] = cost
                    # 새로운 비용으로 갱신 
                    heapq.heappush(q, (cost, dx, dy))

    print(distance[n-1][n-1])
