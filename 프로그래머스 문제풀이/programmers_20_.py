# 프로그래머스 배열 원소의 길이 (level 0)
def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer