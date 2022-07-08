import heapq

n = int(input()) # 숫자 묶음 개수
card = [] # 각 숫자 묶음의 크기
for _ in range(n):
  heapq.heappush(card, int(input()))

result = 0

# 힙에 원소가 1개 남을 때까지
while len(card) != 1:
  # 가장 작은 2개의 카드 묶음 꺼내기
  one = heapq.heappop(card)
  two = heapq.heappop(card)
  # 카드 묶음을 합쳐 다시 삽입
  sum_value = one + two
  result += sum_value
  heapq.heappush(card, sum_value)

print(result)