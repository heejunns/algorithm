# 프로그래머스 JadenCase 문자열 만들기 (level 1)
from string import ascii_letters
def solution(s):
    answer = ""
    x = 0 # 첫번째 문자를 문자인지 숫자인지 판단하고 변환해야하기 때문에 첫번째 문자인지 확인하기 위한 변수
    for i in s: # for 문으로 각각의 문자를 모두 반복 
        if i != " ": # i 가 공백이 아니라면 
            if x == 0: # x가 0이라면
                if i in ascii_letters: # i가 문자라면 
                    answer+=i.upper() # 대문자로 변환 후 저장 
                    x+=1 
                else: # 숫자라면
                    answer+=i
                    x+=1
            elif x != 0: # x가 0이 아니라면 첫번째 문자는 아니라는 뜻이니까 
                answer+=i.lower() # 소문자로 변환 후 저장 
                x+=1
        elif  i == " ": # i가 공백이라면
            answer+=i # 공백 저장
            x = 0 # 공백 후 새로운 단어가 나올꺼고 첫번째 문자인지 판단하기 위해서 공백이 나오면 x는 0으로 초기화 
    return answer