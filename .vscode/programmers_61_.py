# 프로그래머스 가위 바위 보 (level 0)
def solution(rsp):
    answer = ""
    for i in rsp:
        if i == "2":
            answer+="0"
        elif i == "0":
            answer+="5"
        elif i == "5":
            answer+="2"
    return answer