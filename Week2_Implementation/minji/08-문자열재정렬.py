s = input()

alpha = []
num_sum = 0
result = ""

for i in s:
  # 알파벳은 별도의 리스트에 저장
  if i.isalpha():
    alpha.append(i)
  # 숫자는 따로 합계 계산
  else:
    num_sum += int(i)

# 알파벳 오름차순 정렬
alpha.sort()

for i in alpha:
  result += i

# 숫자가 하나라도 있다면 가장 뒤에 삽입
if num_sum != 0:
  result += str(num_sum)

print(result)