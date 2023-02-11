# 프로그래머스 숨어있는 숫자의 덧셈 (2) (level 0)
def solution(my_string):
    answer = 0
    str = ""
    x = ["1","2","3","4","5","6","7","8","9","0"]
    for i in my_string:
        if i not in x and str!="":
            answer+= int(str)
            print(str)
            str = ""
        elif i in x:
            str+=i
    if str!="":
        answer+=int(str)
    return answer