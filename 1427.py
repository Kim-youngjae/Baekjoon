import sys
input = sys.stdin.readline

data = list(map(int, input().rstrip()))
data.sort(reverse=True)

for i in data:
    print(i, end='')