import sys

n = int(sys.stdin.readline())
time = [[0] * 2 for _ in range(n)]

for i in range(n):
    s,e = map(int, sys.stdin.readline().split())
    time[i][0] = s
    time[i][1] = e

time.sort(key= lambda x: (x[1], x[0]))

count = 1
endTime = time[0][1]
for i in range(1, n):
    if(endTime <= time[i][0]):
        count += 1
        endTime = time[i][1]
        
print(count)

'''계속 틀렸다고 하는 이유를 몰랐는데
정렬을 할 때에 종료시간 기준으로 정렬한 뒤 시작시간으로 정렬했을 때 제일 앞쪽에 있는 원소는
제일 처음 시작되는 회의이다.
그래서 이 부분은 고려하지 않고 그 다음 회의 시간을 비교하여야 했는데
이 부분을 생각하지 못했었다.'''