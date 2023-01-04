# 프로그래머스 성격 유형 검사하기 (level 1)
def solution(survey, choices):
    answer = ""
    total = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    for i in range(len(survey)):
        if choices[i] == 1:
            total[survey[i][0]]+=3
        elif choices[i] == 2:
            total[survey[i][0]]+=2
        elif choices[i] == 3:
            total[survey[i][0]]+=1
        elif choices[i] == 5:
            total[survey[i][1]]+=1
        elif choices[i] == 6:
            total[survey[i][1]]+=2
        elif choices[i] == 7:
            total[survey[i][1]]+=3
    if total["R"]>=total["T"]:
        answer+="R"
    elif total["R"]<total["T"]:
        answer+="T"
    if total["C"]>=total["F"]:
        answer+="C"
    elif total["C"]<total["F"]:
        answer+="F"
    if total["J"]>=total["M"]:
        answer+="J"
    elif total["J"]<total["M"]:
        answer+="M"
    if total["A"]>=total["N"]:
        answer+="A"
    elif total["A"]<total["N"]:
        answer+="N"
    
    return answer