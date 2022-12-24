import sys
input = sys.stdin.readline

n = map(int, input())
data = list(map(int, input().split()))
count = 0

for i in range(len(data) - 1):
    swap = False
    for i2 in range((len(data) - i - 1)):
        if (data[i2] > data[i2 + 1]):
            data[i2], data[i2 + 1] = data[i2 + 1], data[i2]
            swap = True;
            count += 1
    if (swap == False):
        break

print(count)


'''
이 문제는 버블정렬이란 이름의 문제이지만 버블 정렬로 해결하기 못하고
병합 정렬을 사용해야 한다. 병합 정렬을 다룬 이후에 다시 오자..'''