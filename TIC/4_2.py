n = int(input())

times = [n, 60, 60]
cnt = 0

for h in range(times[0] + 1):
    # print("시간 = ", h)
    for m in range(times[1]):
        # print("분 = ", m)
        for s in range(times[2]):
            if '3' in str(h) + str(m) + str(s): # 이렇게 시분초를 하나의 문자열로 합치는 생각을 하지 못했다
                cnt += 1
                
print(cnt)