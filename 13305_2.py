# 한번 더 푸는것
import sys
input = sys.stdin.readline

n = int(input()) # 도시의 개수
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

lowest = costs[0]
price = costs[0] * roads[0]

for i in range(1, (n - 1)):
    if(lowest > costs[i]):
        lowest = costs[i]
    price += lowest * roads[i]

print(price)