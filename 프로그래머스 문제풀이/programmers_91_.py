# 프로그래머스 올바른 괄호 (level 2)
def solution(s):
    answer = True
    x = []
    for i in s:
        if i == "(":
            x.append(i)
        elif i == ")":
            if x == []: # x에 꺼낼 ( 가 없다면 짝이 맞지 않는 것이므로 False로 for문 종료
                answer = False
                break
            x.pop()
    if x != []: # for문을 모두 완료하였는데 짝이 없는 ( 가 있다면 False
        answer = False
    return answer