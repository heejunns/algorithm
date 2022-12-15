# 프로그래머스 잘라서 배열로 저장하기 (level 0)
def solution(my_str, n):
    answer = []
    count = 0 
    str = ""
    for i in my_str:
        str+=i
        count+=1
        if count == n:
            answer.append(str)
            str = ""
            count = 0
    if str != "":
        answer.append(str)
    return answer