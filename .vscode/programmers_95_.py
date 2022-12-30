# 프로그래머스 없는 숫자 더하기 (level 1)
def solution(numbers):
    x = [0,1,2,3,4,5,6,7,8,9]
    for i in numbers:
        if i in x:
            x.pop(x.index(i))
    return sum(x)