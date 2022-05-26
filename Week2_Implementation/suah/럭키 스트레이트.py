import sys
input = lambda : sys.stdin.readline().strip()

# 내 풀이
num = input()
half = len(num)//2
front = num[:half]
back = num[half:]
ff, bb = 0, 0
for i in range(half):
    ff += int(front[i])
    bb += int(back[i])

if ff == bb :
    print("LUCKY")
else:
    print("READY")

# 정답
n = input()
length = len(n) # 점수 값의 총 자릿수
summary = 0

# 왼쪽 부분의 자릿수의 합 더하기
for i in range(length // 2):
    summary += int(n[i])

# 오른쪽 부분의 자릿수의 합 빼기
for i in range(length // 2, length):
    summary -= int(n[i])

# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if summary == 0:
    print("LUCKY")
else:
    print("READY")
