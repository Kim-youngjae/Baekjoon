self_nums = set(range(1, 10001))
numbers = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j) # 자릿수를 더해준다
    numbers.add(i)

self_nums = self_nums - numbers

for self_num in sorted(self_nums):
    print(self_num)

'''
집합자료형 set()을 이용하는 생각과 집합 자료형을 - 연산자를 이용해 차집합만 구해주는 아이디어가 필요하였다.
'''