# 프로그래머스 숫자 문자열과 영단어 (level 1)
def solution(s):
    answer = ""
    remember = ""
    x = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6","seven":"7", "eight":"8", "nine":"9"}
    y = ["0","1","2","3","4","5","6","7","8","9"]
    for i in s:
        if i in y: # 숫자라면 answer에 저장 
            answer+=i
        else:
            remember+=i # 아니라면 remember에 저장
        if remember in x: # 저장하다가 x에 포함되는 문자열이 나온다면 
            answer+= x[remember] # answer에 저장
            remember = "" # remember 초기화 

    return int(answer) # int형으로 변환후 반환