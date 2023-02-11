# 프로그래머스 문자열 정렬하기 (1) (level 0)
def solution(my_string):
    x = ["0","1","2","3","4","5","6","7","8","9"]
    answer = []
    for i in my_string:
        if i in x:
            answer.append(int(i))
    answer.sort()
    
    return answer