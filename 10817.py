data = list(map(int, input().split()))

for i in range(len(data) - 1):
    swap = False
    for i2 in range(len(data) - i - 1):
        if(data[i2] > data[i2 + 1]):
            data[i2], data[i2 + 1] = data[i2 + 1], data[i2]
            swap = True
    if (swap == False):
        break

print(data[1])
