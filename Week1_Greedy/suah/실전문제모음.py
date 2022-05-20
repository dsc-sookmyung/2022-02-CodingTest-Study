# 1번 - 큰 수의 법칙 
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

arr.sort()
while m > 0:
    for _ in range(k):
        if m == 0:
            break
        answer += arr[n-1]
        m -= 1
    if m == 0:
        break
    answer += arr[n-2]
    m -= 1

print(answer)


# 2번 - 숫자 카드 게임 
N, M = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(N)]
maxx = 0

for i in range(N):
    temp = min(cards[i])
    if temp > maxx:
        maxx = temp

print(maxx)


# 3번 - 1이 될 때까지 
n, k = map(int, input().split())
count = 0

while n >= 1:
    if n == 1 :
        break
    elif n % k == 0:
        n = n // k
        count += 1
    else :
        n = n-1
        count += 1

print(count)
