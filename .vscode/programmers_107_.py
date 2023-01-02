# 프로그래머스 자연수 뒤집어 배열로 만들기 (level 1)
def solution(n):
    answer = []
    for i in str(n):
        answer.insert(0,int(i))
    return answer