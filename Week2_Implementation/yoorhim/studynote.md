## 구현(Implementation)

![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/5bbce15b-96ac-4924-9149-08be538810ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220527%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220527T100821Z&X-Amz-Expires=86400&X-Amz-Signature=562a246f7d50e9c2abb5e0469ca6723dbc7273ac9957ed33c2143b215e9587ed&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

- 머릿속에 있는 **알고리즘을 소스코드로 바꾸는 과정**
- 흔히 알고리즘 대회에서 구현 유형의 문제란?
    - 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제
- 구현 유형의 예시
    - 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제
    - 실수 연산을 다루고, 특정 소수점까지 출력해야 하는 문제
    - 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
    - 적절한 라이브러리를 찾아서 사용해야 하는 문제
- 일반적으로 알고리즘 문제에서의 2차원 공간은 행렬(Matrix)의 의미

![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/246bb16d-6298-491f-892f-1fd69279a113/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220527%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220527T100839Z&X-Amz-Expires=86400&X-Amz-Signature=89a55d3509419544d0114f4806ccd5ecaefd2159a0a9b2a50963ed7c5d72cc27&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
```python
for i in range(5):
	for j in range(5):
		print('(', i, ',', j, ')', end=' ')
	print()
```
- 시뮬레이션 및 완전 탐색 문제에서는 2차원 공간에서의 방향 벡터가 자주 활용된다.

![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d0e34887-0e8a-4e5c-926d-518d9878576b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220527%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220527T100841Z&X-Amz-Expires=86400&X-Amz-Signature=03558e1a63506ec2f0ee9c6fd8e52f92c16dcc78c152206b9f2c8938ad14b638&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

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
