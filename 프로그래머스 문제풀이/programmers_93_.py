# 프로그래머스 옹알이(2) (level 1)
def solution(babbling):
    answer = 0
    x = ["aya", "ye", "woo", "ma" ]
    for i in babbling:
        str = "" # 문자열을 저장하기 위한 변수
        remember = "" # 하나의 문자열에 한개 이상 이상의 x 리스트의 원소가 있다면 연속적으로 겹치지 않아야 하니까 전에 원소를 기억하는 변수
        for l in i:
            str+=l
            if str in x and str != remember: # x 리스트에 포함되고 remember와 같지 않다면
                remember = str # remember에 저장하고 
                str = "" # str 초기화
        if str == "": # 하나의 문자열을 처리했을때 모두 처리되어 str이 ""이라면 
            answer+=1 # 발음할 수 있는 단어의 개수 +1 
            
    return answer