# 프로그래머스 이상한 문자 만들기 (level 1)
def solution(s):
    answer = ""
    x = 0 # 인덱스값
    for i in s:
        if i == " ": # 공백이면
            answer+=" "
            x = 0 # x를 초기화 
        elif i != " ":
            if x%2 == 0:
                answer+= i.upper()
                x+=1 # 연속해서 문자가 나온다면 인덱스값 +1 
            else:
                answer+= i.lower()
                x+=1 # 연속해서 문자가 나온다면 인덱스값 +1
    return answer