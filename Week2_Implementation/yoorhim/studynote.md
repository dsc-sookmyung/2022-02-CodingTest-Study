## 구현(Implementation)

![Untitled](https://user-images.githubusercontent.com/90624848/170692004-2ff85e43-2ec9-4018-9b2f-130669fc3fd4.png)

- 머릿속에 있는 **알고리즘을 소스코드로 바꾸는 과정**
- 흔히 알고리즘 대회에서 구현 유형의 문제란?
    - 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제
- 구현 유형의 예시
    - 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제
    - 실수 연산을 다루고, 특정 소수점까지 출력해야 하는 문제
    - 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
    - 적절한 라이브러리를 찾아서 사용해야 하는 문제
- 일반적으로 알고리즘 문제에서의 2차원 공간은 행렬(Matrix)의 의미

![Untitled (1)](https://user-images.githubusercontent.com/90624848/170692002-e5327bea-9e8e-46a3-a524-ea96d564ef33.png)
```python
for i in range(5):
	for j in range(5):
		print('(', i, ',', j, ')', end=' ')
	print()
```
- 시뮬레이션 및 완전 탐색 문제에서는 2차원 공간에서의 방향 벡터가 자주 활용된다.

![Untitled (2)](https://user-images.githubusercontent.com/90624848/170691998-913cbfc2-b6d4-4a29-9dbc-87839fd6fad2.png)


```python
# 동, 북, 서, 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 현재 위치
x, y = 2, 2

for i in range(4):
	# 다음 위치
	nx = x + dx[i]
	ny = y + dy[i]
	print(nx, ny)
```
