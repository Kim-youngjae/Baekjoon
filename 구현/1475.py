import math

n = input() # 방번호
nums = [0] * 10 # 체크할 방번호

for i in range(len(n)): # 방번호 번호 하나씩 체크
    nums[int(n[i])] += 1
    
max_sets = nums[0]
# 6, 9 인덱스를 제외하고 제일 큰 값을 찾아야함
for i in range(len(nums)):
    if (i == 6 or i == 9):
        continue
    max_sets = max(max_sets, nums[i])

result = max(math.ceil((nums[6] + nums[9]) / 2), max_sets)
print(result)