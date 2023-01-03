while True:
    try:
        print(input())  
    # 예외가 발생했을 경우 실행되는 코드
    except EOFError: # EOFError가 발생하였을 때 실행
        break


import sys

s = sys.stdin.readlines()

for i in s:
    print(i.rstrip())