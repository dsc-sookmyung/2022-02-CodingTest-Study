# 시계 방향으로 90도 회전하는 함수
def turn(key):
  m = len(key)
  new_key = [[0]*m for _ in range(m)]
  for r in range(m):
    for c in range(m):
      new_key[c][m-1-r] = key[r][c]
  return new_key

# 자물쇠의 중간 부분이 모두 1인지 확인하는 함수
def check(new_lock):
  lock_length = len(new_lock) // 3 # 자물쇠 중간 부분의 길이
  for r in range(lock_length, lock_length*2):
    for c in range(lock_length, lock_length*2):
      if new_lock[r][c] != 1:
        return True
      else:
        return False

def solution(key, lock):
  m = len(key)
  n = len(lock)

  # lock 배열을 가로, 세로 길이가 3배인 새로운 배열의 중앙 부분으로 이동
  new_lock = [[0]*(n*3) for _ in range(n*3)]
  for r in range(n):
    for c in range(n):
      new_lock[r+n][c+n] = lock[r][c]
  
  # key 배열을 새로운 배열의 좌측 상단부터 순서대로 이동시키면서 겹치는 부분만 확인
  for _ in range(4):
    key = turn(key)
    for x in range(n*2):
      for y in range(n*2):
        # 자물쇠에 열쇠 끼워넣기 (*)
        for r in range(m):
          for c in range(m):
            new_lock[x+r][y+c] += key[r][c]
        # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
        if check(new_lock) == True:
          return True
        # 자물쇠에서 열쇠 다시 빼기
        for r in range(m):
          for c in range(m):
            new_lock[x+r][y+c] -= key[r][c]

  return False

print(solution([[0,0,0],[1,0,0],[0,1,1]], [[1,1,1],[1,1,0],[1,0,1]]))