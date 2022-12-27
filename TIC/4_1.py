n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if (plan == move_types[i]):
            # x += dx[i]
            # y += dy[i]
            cx = x + dx[i]
            cy = y + dy[i]
            # 아,,, 이렇게 다른 변수로 초기화하는 이유가 지도를 벗어낫을 때 다시 1로 초기화하기 위함이었다..
    print('current x, y = ', cx, cy)
    if (cx < 1 or cy < 1 or cx > n or cy > n):
        continue
    x, y = cx, cy
print(x, y)