import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        # 우선순위 큐에 (음식 시간, 음식 번호) 형태로 삽입
        heapq.heappush(q, (food_times[i], i+1))

    sum_value = 0  # 먹기 위해 사용한 시간
    previous = 0  # 직전에 다 먹은 음식 시간
    length = len(food_times)  # 남은 음식 개수

    # sum_value + (n번 음식을 먹는 시간 * 남은 음식 개수)가 k보다 클 동안 반복
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1  # 다 먹은 음식 제외
        previous = now  # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인
        answer = sorted(q, key=lambda x: x[1])  # 음식 번호 기준으로 출력
        return answer[(k - sum_value)][1]
