# 프로그래머스 최댓값과 최솟값 (level 2)
def solution(s):
    answer = ''
    x = list(map(int,s.split())) # map 함수를 이용하여 s 문자열을 공백을 기준으로 split() 하고 각각의 요소를 int형으로 변환 후 list에 저장 
    answer+=str(min(x)) # 최소값 str로 변환
    answer+=" "
    answer+=str(max(x)) # 최대값 str로 변환
    
    return answer