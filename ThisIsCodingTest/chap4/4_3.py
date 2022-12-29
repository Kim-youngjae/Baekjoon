pos = input()
row = int(pos[1])
col = int(ord(pos[0])) - int(ord("a")) + 1

steps = [(-1, 2), (1, 2), (-1, -2), (-1, -2), (-2, 1), (-2, -1), (2, 1), (2, -1)]
cnt = 0 # 가능한 움직임을 카운트

for move in steps:
    temp_row = row + move[0]
    temp_col = col + move[1]
    
    if (temp_col < 1 or temp_row < 1 or temp_col > 8 or temp_row > 8):
        continue
    else:
        cnt += 1

print(cnt)


