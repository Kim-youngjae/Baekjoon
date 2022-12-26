import sys
input = sys.stdin.readline


n = int(input()) # 회의의 수
meeting = [[0] * 2 for _ in range(n)]
count = 1

for i in range(n):
    s, e = map(int, input().split())
    s = meeting[i][0]
    e = meeting[i][1]

meeting.sort(key=lambda x: (x[1], x[0]))
endTime = meeting[0][1]

for i in range(n):
    if meeting[i][0] >= endTime:
        endTime = meeting[i][1]
        count += 1
        
print(count)

