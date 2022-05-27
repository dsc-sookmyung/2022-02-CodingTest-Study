import sys
input = lambda : sys.stdin.readline().strip()

# 정답
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

# 만들 수 없는 금액 출력
print(target)

'''
이 문제는 한 번에 푸는게 어려워서 삽질을 여러 번 했는데... 
결국 아이디어 싸움인듯ㅎ
1부터 시작해서 만들 수 있는 숫자 찾아가는 방식이 정답이다

[3, 2, 1, 1, 9] 예시를 들어보면, 먼저 정렬한 상태는 [1, 1, 2, 3, 9]
index=0부터 시작. 만들 수 있는 금액(target)이 1보다 작지 않으므로 target에 1 더해서 target=2가 됨
... target=8까지 계속 진행. 이후에 x인 9보다 target인 8이 작아서 답을 바로 출력! 
'''
