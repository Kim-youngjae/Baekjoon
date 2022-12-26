import sys
input = sys.stdin.readline
cnt = [0] * 3

t = int(input())
if (t % 10 != 0):
    print(-1)
else:
    index = 0
    for i in [300, 60, 10]:
        cnt[index] += t // i
        index += 1
        t %= i
    for i in cnt:
        print(i, end=" ")







# if t % 10 != 0:
#     print(-1)
# else:
#     for i in cnt:
#         print((t // i), end=" ")
#         t %= i