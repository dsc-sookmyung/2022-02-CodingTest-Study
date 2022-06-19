n = int(input())  # 동전의 개수
coins = list(map(int, input().split()))  # 화폐 리스트
coins.sort()  # 오름차순 정렬

target = 1  # 확인하고 싶은 금액

for coin in coins:
    # 추가된 금액이 target보다 크면 절대 못 만듦, 반복 종료
    if target < coin:
        break
    target += coin  # 새로 추가되는 화폐만큼 더해 target 변경

print(target)
