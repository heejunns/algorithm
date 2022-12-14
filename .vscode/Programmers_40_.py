# 프로그래머스 숨어있는 숫자의 덧셈 (1)
from string import ascii_letters
def solution(my_string):
    x = list(ascii_letters)
    answer = 0
    for i in my_string:
        if i not in x:
            answer+= int(i)
    return answer

