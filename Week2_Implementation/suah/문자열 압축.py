import sys
input = lambda : sys.stdin.readline().strip()

# 정답
def solution(s):
    answer = len(s)

    for i in range(1, len(s) // 2 + 1):
        repeat = 1
        string = ''
        temp = s[:i]
        for j in range(i, len(s), i):
            if s[j:i + j] == temp:
                repeat += 1
            else:
                string += str(repeat) + temp if repeat > 1 else temp
                temp = s[j:i + j]
                repeat = 1
        string += str(repeat) + temp if repeat > 1 else temp
        answer = min(answer, len(string))

    return answer
