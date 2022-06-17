n = int(input())  # 보드 크기
k = int(input())  # 사과 개수
data = [[0] * (n+1) for _ in range(n+1)]  # 맵 정보
info = []  # 방향 회전 정보

# 사과 위치
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1  # 사과가 있으면 1로 표시

l = int(input())  # 뱀의 방향 전환 횟수
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 동, 남, 서, 북에 따른 이동 방향
dx = [0, 1, 0, -1]  # x좌표
dy = [1, 0, -1, 0]  # y좌표


def turn(dir, c):
    if c == "L":  # 왼쪽으로 90도 회전 (3 -> 2 -> 1 -> 0 -> 3 -> ...)
        dir = (dir-1) % 4
    else:  # 오른쪽으로 90도 회전 (0 -> 1 -> 2 -> 3 -> 0 -> ...)
        dir = (dir+1) % 4
    return dir


def simulate():
    x, y = 1, 1  # 뱀의 초기 위치
    data[x][y] = 2  # 뱀이 존재하는 위치는 2로 표시
    dir = 0  # 처음에는 동쪽을 보고 있음
    time = 0  # 시작한 후 지나간 시간
    index = 0  # 다음에 회전할 정보
    q = [(x, y)]  # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)
    while True:
        nx = x + dx[dir]
        ny = y + dy[dir]
        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            if data[nx][ny] == 0:  # 사과가 없으면
                data[nx][ny] == 2  # 이동 후
                q.append((nx, ny))  # 위치 기록하고
                px, py = q.pop(0)
                data[px][py] = 0  # 꼬리 제거
            if data[nx][ny] == 1:  # 사과가 있으면
                data[nx][ny] == 2  # 이동 후
                q.append((nx, ny))  # 위치 기록하고 꼬리 그대로 두기
        # 벽이나 뱀의 몸통과 부딪히면 반복문 종료
        else:
            time += 1
            break
        x, y = nx, ny  # 다음 위치로 머리를 이동
        time += 1
        if index < 1 and time == info[index][0]:  # 회전할 시간이 되었을 때
            dir = turn(dir, info[index][1])
            index += 1
    return time


print(simulate())
