# 프로그래머스 영어가 싫어요 (level 0)
def solution(numbers):
    x = {"zero": "0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
    answer = ""
    str = ""
    for i in numbers:
        str+=i
        if str in x:
            answer+= x[str]
            str = ""
    return int(answer)