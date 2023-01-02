n = int(input())
ranks = [0] * n
people = [0] * n
count = 0

for i in range(n):
    data = list(map(int, input().split()))
    people[i] = data

for i in range(n):
    count = 0
    temp_weight = people[i][0]
    temp_height = people[i][1]
    for j in range(n):
        if(temp_weight < people[j][0] and temp_height < people[j][1]):
            count += 1
    ranks[i] = (count + 1)

for i in ranks:
    print(i, end=" ")