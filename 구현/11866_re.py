# import sys
from collections import deque

# input = sys.stdin.readline
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
