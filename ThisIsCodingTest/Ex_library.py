from itertools import permutations, combinations, product

data = ['A', 'B', 'C']

result = list(permutations(data, 3))
print("result = ", result)

result2 = list(combinations(data, 2)) # 순서를 고려하지 않고 나열하는 모든 경우의 수
print("result2 = ", result2)

result3 = list(product(data, repeat=2)) # 2개를 뽑는 모든 경우의 수
# permutation과 같이 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우를 계산
# 대신 원소를 중복하여 뽑는다.
print("result3 = ", result3)
