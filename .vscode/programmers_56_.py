# 프로그래머스 인덱스 바꾸기 (level 0)
def solution(my_string, num1, num2):
    x = []
    for i in my_string:
        x.append(i)
    tmp = x[num1]
    x[num1] = x[num2]
    x[num2] = tmp
    return "".join(x)