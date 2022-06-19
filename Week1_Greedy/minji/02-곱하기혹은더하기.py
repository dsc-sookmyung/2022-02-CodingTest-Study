s = input()
result = int(s[0])

for i in range(1, len(s)):
  # 한 쪽 수가 0이나 1인 경우에는 덧셈이 더 크다
  if result <= 1 or int(s[i]) <= 1:
    result += int(s[i])
  # 이외의 경우에는 항상 곱셈이 더 크다
  else:
    result *= int(s[i])

print(result)