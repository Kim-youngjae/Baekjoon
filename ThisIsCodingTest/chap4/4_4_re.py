n, m = map(int, input().split())
x, y, direc = map(int, input().split())
visit = [[0] * m for _ in range(n)] # 방문 여부 체크
visit[x][y] = 1 # 시작 노드는 당연히 방문 처리를 해줬어야 했다

arr = [] # 지도 생성
for i in range(n):
    arr.append(list(map(int, input().split()))) # 입력받고 리스트로 형변환 해주었어야 했다.

# 북 = 0, 동 = 1, 남 = 2, 서 = 3 별것 아니지만 이게 진짜 중요한 것 같다
# 방향을 설정해서 이동하는 문제는 dx dy 별도의 리스트를 만들어 방향을 정하는 것이 효과적인 것 같다
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn():
    global direc
    direc -= 1 # 왼쪽으로 돌아야 하므로 하나씩 빼준다.
    if direc == -1:
        direc = 3

cnt = 1
turn_time = 0

while True:
    turn()
    nx = x + dx[direc]
    ny = y + dy[direc]
    if (visit[nx][ny] == 0 and arr[nx][ny] == 0): # 방문하지 않고 바다가 아니면
        x = nx
        y = ny
        visit[nx][ny] = 1
        turn_time = 0
        cnt += 1
    else:
        turn_time += 1
    # 4번 다 돌았는데 방문하였거나 바다이면
    if turn_time == 4:
        nx = x - dx[direc]
        ny = y - dy[direc]
        if arr[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(cnt)