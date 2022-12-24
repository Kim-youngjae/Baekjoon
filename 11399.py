import sys
input = sys.stdin.readline

n = int(input())
wait_time = []
data = list(map(int, input().split()))
data.sort()

first = data[0]
for i in range(1, len(data)):
    result = 0
    for j in range(0, i + 1):
        result += data[j]
    wait_time.append(result)
        
print(sum(wait_time) + first)

'''
그리디 문제
기다리는 최소 합을 구하는 문제였다
리스트를 오름차순으로 정렬한 뒤 
순서대로 기다리는 시간의 합을 구하는 부분을 구현하는데 
고민을 좀 하였다
'''
