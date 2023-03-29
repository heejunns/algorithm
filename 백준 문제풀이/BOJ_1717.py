# 백준 11899번, 괄호 끼워넣기
import sys
s = sys.stdin.readline().rstrip() # 괄호열 s 입력받기
result = [] # 짝이 맞지 않은 문자열 저장할 리스트
for i in s: # 입력받은 문자열 s 를 하나씩 꺼내기
    if len(result) == 0: # result 에 아무 문자도 저장되어 있지 않다면 저장
        result.append(i)
    elif result[-1] == "(" and i == ")": # result 에 가장 최근에 저장된 문자가 ( 이고 현재 꺼낸 문자가 ) 라면 짝이 맞으니까 result 에서 ( 꺼내기
        result.pop()
    else: # 위의 조건에 맞지 않다면 result 에 현재 꺼낸 문자 i 저장
        result.append(i)
print(len(result)) # result 의 길이가 올바른 괄호열을 만들기 위해 앞과 뒤에 붙여야 할 괄호의 최소 개수이다.