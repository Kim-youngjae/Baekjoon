import sys
input = sys.stdin.readline

n = int(input()) # 도시의 개수
roads = list(map(int, input().split())) # 도로의 갯수
costs = list(map(int, input().split())) # 도시 마다 기름 값

total = costs[0] * roads[0]
lowest = costs[0]

for i in range(1, len(costs) - 1):
    if(costs[i] < lowest):
        lowest = costs[i]
    total += (roads[i] * lowest)
    

print(total)