n = int(input())
line = 1

while(n > line):
    n -= line
    line += 1

if (line % 2 == 0):
    b = n
    a = line - n + 1
else:
    a = n
    b = line - n + 1

print("{0}/{1}".format(b, a))