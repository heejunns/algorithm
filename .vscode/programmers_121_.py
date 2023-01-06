# 프로그래머스 문자열 다루기 기본 (level 1)
from string import ascii_letters
x = list(ascii_letters)
def solution(s):
    answer = False # s 문자열의 길이가 4, 6이 아니라면 조건에 맞지 않으니까 그대로 False
    if len(s)==4 or len(s) ==6:
        answer = True # 조건에 맞고 아래의 for문에서 각각의 문자 중에서 x에 포함되지 않으면 answer의 값은 바뀌지 않을거고 그렇다는건 문자열 s에 알파벳이 없다는 뜻이니까 True
        for i in s:
            if i in x: # x에 i가 있다면 알파벳이 있다는 말이니까 
                answer = False # False로 저장
                break # 더이상 확인할 필요 없으니까 for문 탈출
    return answer