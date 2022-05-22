n, m = map(int, input().split())  # 볼링공의 개수, 최대 무게
balls = list(map(int, input().split()))  # 각 볼링공의 무게

# 개인 풀이
result1 = 0  # 경우의 수
for i in range(len(balls)):  # 0 ~ n-1
    for j in range(i+1, len(balls)):  # i+1 ~ n
        if balls[i] != balls[j]:
            result1 += 1
print(result1)


# 해설지 풀이 (이해 필요)
array = [0] * 11  # 1부터 10까지 무게를 담는 리스트

for x in balls:
    array[x] += 1  # 각 무게의 개수 카운트

result2 = 0
for i in range(1, m+1):  # 1부터 m까지 각 무게에 대하여 처리
    n -= array[i]  # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result2 += array[i] * n  # B가 선택하는 경우의 수와 곱하기
print(result2)
