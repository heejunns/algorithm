# 프로그래머스 문자열 내 p와 y의 개수 (level 1)
def solution(s):
    answer = True
    count_p = 0 
    count_y = 0
    for i in s:
        if i == "p" or i == "P":
            count_p+=1
        elif i == "y" or i == "Y":
            count_y+=1
    if count_p != count_y: # p와 y가 하나도 없거나 같은 개수인 경우에는 True이고 p와 y의 개수가 다를때만 False
        answer = False  
    return answer