import sys
input = sys.stdin.readline

n = int(input())

maxWeight = [] # 최대 중량을 저장할 리스트
ropeList = [0] * n # 로프의 최대중량을 저장할 리스트

for i in range(n):
    ropeList[i] = int(input())

ropeList.sort(reverse=True) # 리스트 내림 차순 정렬

for i in range(len(ropeList)):
    weight = ropeList[i] * (i + 1)
    maxWeight.append(weight)

maxWeight.sort()

print(maxWeight[-1])

'''
문제가 무엇을 요구하는지 몰라서 코드를 보진 않았지만 문제 접근 방식을 보았다
예시를 적절하게 들어서 해결하려고 노력해보자'''