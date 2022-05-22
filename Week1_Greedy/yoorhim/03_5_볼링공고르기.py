n, m = map(int, input().split())
data = list(map(int, input().split()))

weight = [0] * 11
result = 0

"""
첫 번째 풀이: 시간 복잡도가 O(n^2)
for i in range(len(data)):
    for j in range(i+1, len(data)):
        if data[i] != data[j]:
            result += 1
"""

for w in data:
    weight[w] += 1

for i in range(len(data)):
    result += weight[i] * sum(weight[i+1:])

"""
답안 예시
for i in range(1, m + 1):
    n -= array[i]
    result += array[i] * n
"""
print(result)


