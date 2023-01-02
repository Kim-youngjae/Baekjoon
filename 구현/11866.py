import sys
from collections import deque

input = sys.stdin.readline
deque = deque()
result = []

n, k = map(int, input().split())

for i in range(1, n + 1):
    deque.append(i)

while deque: # 덱이 비었을 때 까지 비었으면 while 종료
    for i in range(k - 1):
        deque.append(deque.popleft())
    result.append(deque.popleft())

print("<", end="")
print(", ".join(map(str, result)), end=">")

'''
큐로만 기능을 구현하려고 하였는데 계속 시간 초과가 떠서 솔루션을 찾아보니 deque이라는 기능을 구현하여 사용하였다
큐와 스택의 기능, 원하는 위치에 값을 추가하고 삭제하는 기능까지 있는 자료구조였다.'''