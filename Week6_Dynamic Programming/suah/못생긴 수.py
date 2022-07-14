'''
Q35. 못생긴 수 

<문제> 
- 못생긴 수 == 오직 2, 3, 5를 약수로 갖는 수 
- 1은 못생긴 수라고 가정 
- n번째 못생긴 수 찾는 프로그램 
- ex) {1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, ...}
'''

import sys 
input = lambda : sys.stdin.readline().strip()

n = int(input())
dp = [False] * 1001
dp[1] = True 

for i in range(2, 1001):
	if i%2 == 0:
		dp[i] = True
		
	elif i%3 == 0: 
		dp[i] = True 

	elif i%5 == 0:
		dp[i] = True

result = [i for i in range(len(dp)) if dp[i] == True]
print(result[n-1])
