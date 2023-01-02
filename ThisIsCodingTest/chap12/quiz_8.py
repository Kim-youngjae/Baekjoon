n = input()
data = []
total = 0
for text in n:
    if (str.isdigit(text)): # 문자열이 정수인지 문자 그자체인지 판별해주는 함수 정수이면 True, 아니면 False반환
        total += int(text)
    else:
        data.append(text)
        
data.sort()

for i in data:
    print(i, end="")
print(total)