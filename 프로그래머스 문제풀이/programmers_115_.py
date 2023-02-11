# 프로그래머스 크기가 작은 부분문자열 (level 1)
def solution(t, p):
    answer = 0
    x = 0
    y = len(p) # 문자열 p의 길이만큼 부분문자열을 만들기 위해 
    strs = ""
    while x <= len(t)-len(p): # 부분문자열을 만들기위한 인덱스의 범위
        strs +=t[x:y] 
        if int(p) >= int(strs): 
            answer+=1
        x+=1
        y+=1
        strs = ""
        