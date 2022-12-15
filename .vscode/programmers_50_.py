# 프로그래머스 OX퀴즈 (level 0)
def solution(quiz):
    answer = []
    for i in quiz:
        result = 0
        x = i.split()
        if x[1] == "+":
            result = int(x[0])+int(x[2])
        elif x[1] == "-":
            result = int(x[0])-int(x[2])
        elif x[1] == "*":
            result = int(x[0])*int(x[2])
        elif x[1] == "/":
            result = int(x[0])/int(x[2])
        elif x[1] == "%":
            result = int(x[0])%int(x[2])
        if x[4] == str(result):
            answer.append("O")
        else:
            answer.append("X")
    return answer