# 프로그래머스 문자 반복 출력하기 (level 0)
def solution(my_string, n):
    answer = ""
    for i in my_string:
        answer+= i*n
    return answer
