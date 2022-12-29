n = input() # 현재 캐릭터의 점수

data = []
for i in n:
    data.append(i)
    
# 자릿수 기준으로 n을 반으로 나눔

left = [0] * (int(len(n)) // 2)
right = [0] * (int(len(n)) // 2)
m = len(data) // 2

for i in range(len(data)):
    if (i < m):
        left[i] = data[i]
    else:
        right[i - m] = data[i]
        
sum_l = 0
sum_r = 0

for i in range(m):
    sum_l += int(left[i])
    sum_r += int(right[i])
    
if sum_l - sum_r == 0:
    print("LUCKY")
else:
    print("READY")