import sys
input = sys.stdin.readline

formula = list(map(str, input().rstrip().split('-')))
data = []

for num1 in formula:
    result = 0
    s = num1.split('+')
    for num2 in s:
        result += int(num2)
    data.append(result)

result = data[0]
for i in range(1, len(data)):
    result -= data[i]
    
print(result)

"""
split()으로 -, +를 구분하여 연산을 진행하면 되는 문제였다.
이 문제는 자바에서도 이렇게 문자열을 특정 기호 단위로 자를 수 있는게 있는지 찾아보아야겠다.
"""