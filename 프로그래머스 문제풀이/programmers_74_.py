# 프로그래머스 2차원으로 만들기 (level 0)
def solution(num_list, n):
    answer = []
    x = []
    for i in num_list:
        x.append(i)
        if len(x) == n:
            answer.append(x)
            x = [] 
    return answer