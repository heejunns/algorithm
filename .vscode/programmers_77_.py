# 프로그래머스 문자열 나누기 (level 0)
def solution(s):
    answer = 0
    str = ""
    count = 0
    count_1 = 1
    for i in s:
        if str == "": # str에 아무것도 없다면 
            str+= i
            count+=1
        elif str == i: # 저장된 str과 i가 같다면 
            count+=1
        elif str!=i and count_1 != count: # 저장된 str과 다르고 count의 개수가 다르다면 
            count_1+=1
        elif str!=i and count == count_1: # count와 개수가 같아지면 이제 분리 
            count = 0
            count_1 = 1
            str = ""
            answer+=1
    if str != "": # 마지막 남은 str이 있다면 
        answer+=1
        
    return answer