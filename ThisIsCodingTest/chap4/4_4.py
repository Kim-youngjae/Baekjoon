n, m = map(int, input().split()) # n행 m열
x, y, direction = map(int, input().split()) # a, b 캐릭터의 위치 d 보고 있는 방향
visit = [[0] * m for _ in range(n)] # 방문할 위치를 저장할 맵
visit[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북서남동 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if (direction == -1):
        direction = 3

cnt = 1
turn_time = 0

while(True):
    turn_left()
    nx = x + dx[direction] #현재위치 x
    ny = y + dy[direction] # 현재 y 위치
    if (visit[nx][ny] == 0 and array[nx][ny] == 0):
        visit[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        print("nx, ny =  {}, {}, {} x, y = {}, {}".format(nx, ny, direction, x, y))
        nx = x - dx[direction]
        ny = y - dy[direction]
        if (array[nx][ny] == 0):
            x = nx
            y = ny
            print(x, y)
        else:
            break
        turn_time = 0

print(cnt)